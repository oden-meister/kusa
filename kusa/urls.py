from django.urls import path
from rest_framework import routers
from . import views
from .views import raspberryViewSet,SmileSViewSet,SmileIViewSet

router=routers.DefaultRouter()
router.register(r'raspberrys',raspberryViewSet)
router.register(r'SmileIs',SmileIViewSet)
router.register(r'SmileSs',SmileSViewSet)

app_name='kusa'

urlpatterns=[
    path('', views.index, name='index'),
    path("info/",views.info,name='info'),
    path('rasplist/',views.raspid,name='pk'),
    path('raspsp/<int:pk>/',views.raspsp,name='raspsp'),
]