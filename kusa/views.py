# Create your views here.

from django.template import loader
from django.shortcuts import render
from .models import raspberry,SmileS,SmileI

def index(request):
    return render(request,'kusa/index.html')

def raspid(request):
    latest_raspb_list=raspberry.objects.order_by('-pub_date')[:5]
    context={'latest_raspb_list':latest_raspb_list}
    return render(request, 'kusa/rasplist.html', context)

def raspsp(request,rid):
    raspbid=raspberry.objects.get(id=rid).raspid
    smileI_list=raspberry.objects.get(id=rid).smilei_set.order_by('-pushed_dateI')
    smileS_list=raspberry.objects.get(id=rid).smiles_set.order_by('-pushed_dateS')
    smilei=raspberry.objects.get(id=rid).smilei_set.get(id=rid).smileic
    smiles=raspberry.objects.get(id=rid).smiles_set.get(id=rid).smilesc
    context={
        'smileI_list':smileI_list,
        'smileS_list':smileS_list,
        'smilei':smilei,
        'smiles':smiles,
        'raspbid':raspbid
    }
    return render(request,'kusa/raspsp.html',context)