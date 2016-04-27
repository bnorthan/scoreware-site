from django.http import HttpResponse
from django.shortcuts import render
from .models import Member
from .models import Race
from .models import Result

from django.shortcuts import get_object_or_404, render

import django_tables2 as tables
from django_tables2 import RequestConfig

# Create your views here.
def index(request):
    l_members=Member.objects.all()
    context= {'l_members':l_members}
    return render(request, 'results/index.html', context)

def detail(request, runner_id):
    return HttpResponse("This is runner: %s." % runner_id)

def results(request, runner_id):
    response="You are looking at results of runner %s"
    return HttpResponse(response%runner_id)

def addresult(request, runner_id):
    return HttpResponse("you are adding result for runner %s."%runner_id)

def races(request):
    races=Race.objects.all()
    return render(request, 'races/index.html', {'l_races':races})


class SimpleRace(tables.Table):
    class Meta:    
        #model=Result
        attrs={"class":"paleblue"}
  
    first_name=tables.Column()
    last_name=tables.Column()
    
    gender=tables.Column()
    age=tables.Column()
    city=tables.Column()
    state=tables.Column()
    
    split1=tables.Column()
    splits=tables.Column()

    time=tables.Column()
    
    def render_time(self, value):
        return value.strftime('%M:%S')

'''
    testles=tables.Column(empty_values=())

    def render_testles(self, value):
        return 4
'''
def simple_with_splits():

    def render_split(self, value, record):
        print splits
        if (record.splits==None): return 'Na'
       
        return record.splits.split(',')[0]

    

    attrs={"testbest":tables.Column(empty_values=()),"class":"paleblue"}
   
    attrs['Meta'] = type('Meta', (), dict(attrs={"class":"paleblue", "orderable":"True", "width":"100%"}))  
    attrs['render_testbest']=render_split
    
    klass=type('SimpleWithSplits',(SimpleRace,),attrs)
    return klass

from django.forms.models import model_to_dict

def race(request, race_id):
    race=[]

    results=Race.objects.get(pk=race_id).result_set.all()

    for r in results:
        #temp={}
        temp=model_to_dict(r)
        temp['name']=r.first_name
        splits=r.splits

        if (splits!=None):
            temp['split1']=splits.split(',')[0]
        else:
            temp['split1']='Na'
        race.append(temp)


    
    #race=SimpleRace(Race.objects.get(pk=race_id).result_set.all())
    #race=Race.objects.get(pk=race_id).result_set.all()
    #race=simple_with_splits()(Race.objects.get(pk=race_id).result_set.all())
    race=SimpleRace(race)
    
    RequestConfig(request).configure(race)
    
    return render(request, 'race/index.html', {'l_race':race})







