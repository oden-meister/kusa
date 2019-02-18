from rest_framework import serializers
from .models import raspberry,SmileI,SmileS

class raspberrySerializer(serializers.ModelSerializer):
    class Meta:
        model=raspberry
        fields=('raspid','pub_date',)

class SmileISerializer(serializers.ModelSerializer):
    class Meta:
        model=SmileI
        fields=('rasp','smileic','pushed_dateI',)

class SmileSSerializer(serializers.ModelSerializer):
    class Meta:
        model=SmileS
        fields=('rasp','smilesc','pushed_dateS',)