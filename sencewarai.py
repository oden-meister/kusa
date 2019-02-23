import pandas as pd
import numpy as np
import pyaudio
import scipy.signal
import scipy.fftpack
import scipy.fftpack.realtransforms
import wave
import csv
import time
import subprocess
from sklearn .neighbors import KNeighborsClassifier
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

def wavread(filename):
  wf = wave.open(filename, "r")
  fs = wf.getframerate()
  x = wf.readframes(wf.getnframes())
  x = np.frombuffer(x, dtype="int16") / 32768.0
  wf.close()
  return x, float(fs)

def hz2mel(f):
  return 1127.01048 * np.log(f / 700.0 + 1.0)

def mel2hz(m):
  return 700.0 * (np.exp(m / 1127.01048) - 1.0)

def melFilterBank(fs, nfft, numChannels):
  fmax = fs / 2
  melmax = hz2mel(fmax)
  nmax = nfft / 2
  df = fs / nfft
  dmel = melmax / (numChannels + 1)
  melcenters = np.arange(1, numChannels + 1) * dmel
  fcenters = mel2hz(melcenters)
  indexcenter = np.round(fcenters / df)
  indexstart = np.hstack(([0], indexcenter[0:numChannels - 1]))
  indexstop = np.hstack((indexcenter[1:numChannels], [nmax]))
  filterbank = np.zeros((numChannels, int(nmax)))
  for c in np.arange(0, numChannels):
      increment= 1.0 / (indexcenter[c] - indexstart[c])
      for i in np.arange(indexstart[c], indexcenter[c]):
          i=int(i)
          filterbank[c, i] = (i - indexstart[c]) * increment
      decrement = 1.0 / (indexstop[c] - indexcenter[c])
      for i in np.arange(indexcenter[c], indexstop[c]):
          i=int(i)
          filterbank[c, i] = 1.0 - ((i - indexcenter[c]) * decrement)
  return filterbank, fcenters

def preEmphasis(signal, p):
  return scipy.signal.lfilter([1.0, -p], 1, signal)

def mfcc(signal, nfft, fs, nceps):
  p = 0.97
  signal = preEmphasis(signal, p)
  hammingWindow = np.hamming(len(signal))
  signal = signal * hammingWindow
  spec = np.abs(np.fft.fft(signal, nfft))[:int(nfft/2)]
  fscale = np.fft.fftfreq(nfft, d = 1.0 / fs)[:int(nfft/2)]
  numChannels = 20
  df = fs / nfft
  filterbank, fcenters = melFilterBank(fs, nfft, numChannels)
  mspec = np.log10(np.dot(spec, filterbank.T))
  ceps = scipy.fftpack.realtransforms.dct(mspec, type=2, norm="ortho", axis=-1)
  return ceps[:nceps]

def get_feature(wavfile,nfft,nceps):
  wav, fs = wavread(wavfile)
  t = np.arange(0.0, len(wav) / fs, 1/fs)
  center = len(wav) / 2
  cuttime = 0.8
  wavdata = wav[int(center - cuttime/2*fs) : int(center + cuttime/2*fs)]
  ceps = mfcc(wavdata, nfft, fs, nceps)
  return ceps.tolist()

warai=pd.read_csv("/home/minfaox3/sence-warai/datasets_warai.csv")
waraidf=pd.DataFrame(warai)
y_train=waraidf.label
x_train=waraidf.drop('label',axis=1)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
start=time.time()
while True:
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    wavfile="output.wav"
    nfft=2048
    nceps=12
    tmp=get_feature(wavfile,nfft,nceps)
    f=open('cache.csv','w+')
    writer=csv.writer(f,lineterminator='\n')
    writer.writerow('anticipation')
    writer.writerow(tmp)
    f.close()
    testdata=pd.read_csv("cache.csv")
    testdf=pd.DataFrame(testdata)
    x_testna=testdf[0:1]
    X_new=x_testna.values
    prediction1 = knn.predict(X_new)
    print(prediction1)
    #if prediction1==1:
        #res=subprocess.call(["curl","localhost:3000/mt"])
    elapsed_time = time.time() - start
    #if elapsed_time>=10:
      #print(elapsed_time)
      #start=time.time()
      #subprocess.call(["curl",""])