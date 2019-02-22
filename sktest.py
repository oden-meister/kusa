import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn .neighbors import KNeighborsClassifier
#from pandas.plotting import scatter_matrix
warai=pd.read_csv("/home/minfaox3/sence-warai/datasets_warai.csv")
waraidf=pd.DataFrame(warai)
y_train=waraidf.label
x_train=waraidf.drop('label',axis=1)
#grr=scatter_matrix(x_train,c=y_train,alpha=0.5,figsize=(20,20),marker='o',hist_kwds={'bins' : 20},s=100,cmap=mglearn.cm3)
#plt.show()
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
testco=1
testct=0
for i in range(3):
    testdata=pd.read_csv("/home/minfaox3/sence-warai/testdata.csv")
    testdf=pd.DataFrame(testdata)
    y_ans=testdf.label
    x_testdf=testdf.drop('label',axis=1)
    X_new=np.array([[x_testdf[testct:testco]]])
    prediction1 = knn.predict(X_new)
    print(prediction1)
    testco+=1
    testct+=1