from django.urls import path
from rest_framework import routers
from . import views
from .views import raspberryViewSet,SmileSViewSet,SmileIViewSet

router=routers.DefaultRouter()
router.register(r'raspberrys',raspberryViewSet)
router.register(r'SmileIs',SmileIViewSet)
router.register(r'SmileSs',SmileSViewSet)

urlpatterns=[
    path('',views.index,name='index'),
    path('rasplist/',views.raspid,name='pk'),
    path('raspsp/<int:rid>/',views.raspsp,name='raspsp'),
]