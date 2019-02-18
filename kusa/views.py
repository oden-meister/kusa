# Create your views here.

from rest_framework import viewsets,permissions
from django.shortcuts import render
from .models import raspberry,SmileI,SmileS
from .serializer import raspberrySerializer,SmileISerializer,SmileSSerializer
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def index(request):
    return render(request,'kusa/index.html')

def info(request):
    return render(request,'kusa/info.html')

def raspid(request):
    latest_raspb_list=raspberry.objects.order_by('-pub_date')
    context={'latest_raspb_list':latest_raspb_list}
    return render(request, 'kusa/rasplist.html', context)

def raspsp(request,pk):
    raspbid=raspberry.objects.get(id=pk).raspid
    raspnum=pk
    smileI_list=raspberry.objects.get(id=pk).smilei_set.order_by('-pushed_dateI')[:5]
    smileS_list=raspberry.objects.get(id=pk).smiles_set.order_by('-pushed_dateS')
    left=np.array([1,2,3,4,5])
    height=np.array([0,0,0,0,0])
    flag=0
    for rasp in smileI_list:
        height=np.insert(height,flag,rasp.smileic)
        height=np.delete(height,5)
        flag+=1
    plt.plot(left,height)
    plt.savefig('kusa/static/kusa/figure.png')
    context={
        'smileI_list':smileI_list,
        'smileS_list':smileS_list,
        'raspbid':raspbid,
        'raspnum':raspnum
    }
    return render(request,'kusa/raspsp.html',context)

def mainindex(request):
    return render(request,'oden/index.html')

class raspberryViewSet(viewsets.ModelViewSet):
    queryset = raspberry.objects.all()
    serializer_class = raspberrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SmileIViewSet(viewsets.ModelViewSet):
    queryset = SmileI.objects.all()
    serializer_class = SmileISerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SmileSViewSet(viewsets.ModelViewSet):
    queryset = SmileS.objects.all()
    serializer_class = SmileSSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)