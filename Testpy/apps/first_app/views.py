from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Job
import bcrypt
import django.utils.timezone
from django.urls import reverse
from urllib.parse import urlencode



def index(request):

	return render(request, 'first_app/login.html')

def create(request):
	errors = User.objects.validation(request.POST)
	if len(errors):
		for keys, value in errors.items():
			messages.error(request, value, extra_tags='reg')

		return redirect('/')
	else:
		hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		print(hash)
		new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hash)
		request.session['user_id'] = new_user.id
		return redirect('/home')
	return redirect('/')

def read(request):
	error = User.objects.login_validation(request.POST)
	if len(error):
		for keys, value in error.items():
			messages.error(request, value, extra_tags='login')

		return redirect('/')
	else:
		request.session['user_id'] = User.objects.get(email = request.POST['username']).id
		return redirect('/home')



def home(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'all_jobs' : Job.objects.all()
	}
	return render(request, 'first_app/home.html', context)

def logoff(request):
	request.session.clear()
	return redirect('/')

def addJob(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id'])
	}
	return render(request, 'first_app/addJob.html' , context)

def processAdd(request):
	error = Job.objects.addJobValidations(request.POST)
	if len(error):
		for keys, value in error.items():
			messages.error(request, value, extra_tags='job')

		return redirect('/addJob')
	else:
		Job.objects.create(title = request.POST['title'] , description = request.POST['desc'], location = request.POST['location'], job_from_user_id = request.session['user_id'])
		return redirect('/home')

def displayEdit(request, id):
	request.session['edit'] = id
	context = {
	'Job' : Job.objects.get(id = id)
	}
	print(context)
	return render(request, 'first_app/editjob.html', context)

def displayView(request, id):
	data = Job.objects.get(id = id)
	context = {
	'Job' : data
	}
	return render(request, 'first_app/viewJob.html', context)

def delete(request, id):
	Job.objects.get(id = id).delete()
	return redirect('/home')

def displayEditwErrors(request):
	context = {
	'Job' : Job.objects.get(id = request.session['edit'])
	}
	print(context)
	return render(request, 'first_app/editjobErrors.html', context)

def processEdit(request,id):
	error = Job.objects.addJobValidations(request.POST)
	if len(error):
		for keys, value in error.items():
			messages.error(request, value, extra_tags='job')
		return redirect('/edit/'+str(id))
	else:
		j = Job.objects.get(id = request.session['edit'])
		j.title = request.POST['title']
		j.description = request.POST['desc']
		j.location = request.POST['location']
		j.updated_at = django.utils.timezone.now
		j.save()


		return redirect('/home')

