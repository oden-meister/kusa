from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('rasplist/',views.raspid,name='pk'),
    path('raspsp/<int:rid>/',views.raspsp,name='raspsp'),
]