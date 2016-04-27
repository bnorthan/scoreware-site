from __future__ import unicode_literals

from django.db import models
from localflavor.us.models import USStateField

GENDER_CHOICES=(
        ('M', 'M'),
        ('F', 'F')
    )

# Create your models here.
class Member(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    city=models.CharField(max_length=200, blank=True)
    state=USStateField(blank=True)
    
    date_birth=models.DateTimeField('date of birth')


    def __str__(self):
        return self.first_name+" "+self.last_name
from django.contrib import admin

class Race(models.Model):
    race_name=models.CharField(max_length=200)

    def __str__(self):
        return self.race_name

class Result(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    city=models.CharField(max_length=200, blank=True, null=True)
    state=USStateField(blank=True,null=True)
    bib=models.IntegerField(default='0')
    age=models.IntegerField(default='0')
    time=models.TimeField()
    pace=models.TimeField(default='00:00')
    splits=models.CharField(max_length=400, default='00:00', blank=True, null=True)
    
    race=models.ForeignKey(Race, on_delete=models.CASCADE)
    member=models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)

    def timestring(self):
        try:
            if (self.time!=None):
                timestring=self.time.strftime('%M:%S')
            else:
                timestring='00:00'
        except:
            timestring='00:00'

        return timestring

    def __str__(self):

        return str(self.first_name+" "+self.last_name+" "+self.timestring())



    
