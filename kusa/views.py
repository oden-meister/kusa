# Create your views here.

from rest_framework import viewsets,permissions
from django.shortcuts import render
from .models import raspberry,SmileI,SmileS
from .serializer import raspberrySerializer,SmileISerializer,SmileSSerializer

def index(request):
    return render(request,'kusa/index.html')

def raspid(request):
    latest_raspb_list=raspberry.objects.order_by('-pub_date')[:5]
    context={'latest_raspb_list':latest_raspb_list}
    return render(request, 'kusa/rasplist.html', context)

def raspsp(request,pk):
    raspbid=raspberry.objects.get(id=pk).raspid
    smileI_list=raspberry.objects.get(id=pk).smilei_set.order_by('-pushed_dateI')
    smileS_list=raspberry.objects.get(id=pk).smiles_set.order_by('-pushed_dateS')
    context={
        'smileI_list':smileI_list,
        'smileS_list':smileS_list,
        'raspbid':raspbid
    }
    return render(request,'kusa/raspsp.html',context)

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