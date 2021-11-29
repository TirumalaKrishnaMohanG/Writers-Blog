#!/usr/bin/env python3

# Headers
import pandas as pd
import uuid,datetime,json

from . import serializers
from tabulate import tabulate
from .models import blogarticle
from rest_framework import viewsets
from .models import comment as article
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .serializers import storyseriesapiserializerarticle

# Create your views here.

# Home API
def home(request):
	context = {}
	bVal = blogarticle.objects.all()
	context['data'] = blogarticle.objects.all()
	return render(request,'index.html',context)


# Write API
def write(request):
	return render(request,'write.html')

def writemod(request):
	if request.method == 'POST':
		username = request.POST.get('name')
		title = request.POST.get('title')
		email = request.POST.get('email')
		story = request.POST.get('story')
		refId = username+'_'+str(uuid.uuid1())+datetime.datetime.now().strftime('%Y%m%d_%M%S')
		print(refId)
		samId = 'Sample-565656401-20211701'
		val = blogarticle(name=username, email=email, title=title, story=story, refid=refId)
		finVal = val.save()
		bVal = blogarticle.objects.all()
		print(bVal)
	return render(request,'write.html')

# Comment API
def comment(request):
	context,getList = {},[]
	getCmt = request.POST.get('path')
	getId = request.POST.get('getid')
	getName = request.POST.get('getName')
	getstory = request.POST.get('getstory')
	getfeedback = request.POST.get('getfeedback')
	print(getId)
	# Info Fetch
	# finF = article.objects.values()
	# finTab = pd.DataFrame(finF)
	# filPan = finTab[finTab['refid'] == getId]
	# print(filPan)
	inf = article(name=getName, story=getstory, feedback=getfeedback, refid=getId)
	finInf = inf.save()
	# Mod Url
	modURL = 'http://localhost:8000'+getCmt
	return redirect(modURL)

# View API
def seenstory(request,id):
		context = {}
		context['dataInfo'] = article.objects.all()
		context['getInfo'] = blogarticle.objects.get(id=id)
		return render(request,'view.html',context)

# Rest Framework API starts here
class StoryseriesViewSet(viewsets.ModelViewSet):
	queryset = article.objects.all()
	#qset = article.objects.all()
	#serializer_class = serializers.storyseriesapiserializerblogarticle
	serializer_class = serializers.storyseriesapiserializerarticle