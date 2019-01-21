from django.shortcuts import render, HttpResponse, redirect

def index(request):
	number = 'placeholder'
	return HttpResponse(number)

def new(request):
	new = 'new'
	return HttpResponse(new)

def create(request):
	return redirect('/')

def showNum(request, num):
	yo = "This will display " +num
	return HttpResponse(yo)

def editNum(request, num):
	hi = "edit blog "+num
	return HttpResponse(hi)

def deleteNum(request, num):
	return redirect('/')
	

# Create your views here.
