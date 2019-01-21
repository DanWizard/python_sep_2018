from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    User.objects.initialize(request.session)
    return render(request, 'exam/index.html')

def register(request):
    errors = User.objects.validation(request.POST, request.session)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        user = User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        return redirect('/travels')
    

def login(request):
    errors = User.objects.login(request.POST)
    if errors is not None:
        for key, value in errors.items():
            messages.warning(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        return redirect('/travels')

def success(request):
    info = User.objects.info(request.session)
    mytrips = Trip.objects.mytrips(request.session)
    joinedtrips = Trip.objects.filter(users=request.session['id'])
    others = Trip.objects.exclude(users=request.session['id'])
    context = {
            'info': info,
            'mytrips': mytrips,
            'othertrips': others,
            'joined': joinedtrips
    }
    return render(request, 'exam/dashboard.html', context)

def add(request):
    return render(request, 'exam/add.html')

def addtrip(request):
    errors = Trip.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add')
    else:
        Trip.objects.create(dest=request.POST['destination'], desc=request.POST['description'], start=request.POST['travel_start'], end=request.POST['travel_end'], creator_id=request.session['id'])
        return redirect('/travels')

def join(request, id):
    Trip.objects.join(id, request.session)
    return redirect('/travels')

def show(request, id):
    trip = Trip.objects.get(id=id)
    creator = User.objects.get(id=trip.creator_id).first_name
    joinedusers = User.objects.filter(trips1=id).values()
    print(joinedusers)
    context = {
        'tripdata': trip,
        'creator': creator,
        'joineduser': joinedusers
    }
    return render(request, 'exam/view.html', context)

def cancel(request, id):
    Trip.objects.cancel(id, request.session)
    return redirect('/travels')

def delete(request, id):
    Trip.objects.delete(id)
    return redirect('/travels')

def logout(request):
    request.session.clear()
    return redirect('/')