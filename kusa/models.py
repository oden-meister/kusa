import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class raspberry(models.Model):
    raspid=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.raspid
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class SmileI(models.Model):
    rasp=models.ForeignKey(raspberry,on_delete=models.CASCADE)
    smileic=models.IntegerField()
    pushed_dateI=models.DateTimeField('date published')
    def __int__(self):
        return self.smileic
    def was_published_recently(self):
        return self.pushed_dateI >= timezone.now() - datetime.timedelta(days=1)

class SmileS(models.Model):
    rasp=models.ForeignKey(raspberry,on_delete=models.CASCADE)
    smilesc=models.IntegerField()
    pushed_dateS=models.DateTimeField('date published')
    def __int__(self):
        return self.smilesc
    def was_published_recently(self):
        return self.pushed_dateS >= timezone.now() - datetime.timedelta(days=1)