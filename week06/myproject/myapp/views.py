from django.shortcuts import render 
from django.http import JsonResponse 

def home(request): 
	# View code here... 
	return render(request, 'home.html', {'mykey': 'myvalue'}) 

def blank(request): 
	return render(request, 'blank.html', {'title': 'MyTitle'}) 

def myjson(request): 
	return JsonResponse({'foo': 'bar'})