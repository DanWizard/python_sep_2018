from django.db import models
import re
import bcrypt
from time import strftime, localtime, strptime, mktime

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z- ]+$')

class UserManager(models.Manager):
    def initialize(self, session):
        if 'fname' not in session:
            session['fname'] = ""
        if 'lname' not in session:
            session['lname'] = ""
        if 'email' not in session:
            session['email'] = ""

    def validation(self, postData, session):
        errors = {}
        emails = User.objects.filter(email=postData['email']).all()
        if len(postData['first_name']) < 2:
            errors['fname'] = "First name must be atleast 2 characters and only consist of letters." 
        elif not NAME_REGEX.match(postData['first_name']):
            errors['fname_chars'] = "Name can only contain letters, spaces, or hyphens."
        else:
            session['fname'] = postData['first_name']
        if len(postData['last_name']) < 2:
            errors['lname'] = "Last name must be atleast 2 characters and only consist of letters."
        elif not NAME_REGEX.match(postData['last_name']):
            errors['lname_chars'] = "Name can only contain letters, spaces, or hyphens."
        else:
            session['lname'] = postData['last_name']
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."
        elif len(emails) > 0:
            errors['used'] = "Email has already been registered."
        else:
            session['email'] = postData['email']
        if len(postData['password']) < 8:
            errors['pass_length'] = "Password must be atleast 8 characters."
        elif re.search('[0-9]', postData['password']) is None:
            errors['pass_digit'] = "Password must contain atleast one digit (0-9)."
        elif re.search('[A-Z]', postData['password']) is None:
            errors['pass_cap'] = "Password must contain atleast one capital letter."   
        if postData['confirm_pw'] != postData['password']:
            errors['confirm_pw'] = "Does not match password."
        return errors
    
    def login(self, postData):
        errors = {}
        user_length = User.objects.filter(email=postData['email'])
        if len(user_length) < 1:
            errors['login'] = "Check email/password."
            return errors
        user = User.objects.get(email=postData['email'])
        if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors['login'] = "Check email/password."
            return errors

    def info(self, session):
        info = User.objects.get(id=session['id'])
        return info

class TripManager(models.Manager):
    def validate(self, postData):
        errors = {}
        startdate = postData['travel_start']
        enddate = postData['travel_end']
        start_date = strptime(startdate, "%Y-%m-%d")
        end_date = strptime(enddate, "%Y-%m-%d")
        now = localtime()
        if start_date < now:
            errors['start'] = "Must start before current date."
        if end_date < start_date:
            errors['end'] = "Must end after start date."
        return errors


    def mytrips(self, session):
        mytrips = Trip.objects.filter(creator_id=session['id'])
        return mytrips

    def join(self, id, session):
        this_trip = Trip.objects.get(id=id)
        this_user = User.objects.get(id=session['id'])
        this_user.trips1.add(this_trip)

    def cancel(self, id, session):
        this_trip = Trip.objects.get(id=id)
        this_user = User.objects.get(id=session['id'])
        this_user.trips1.remove(this_trip)

    def delete(self, id):
        trip = Trip.objects.get(id=id)
        trip.deactivated = "Y"
        trip.save()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Trip(models.Model):
    dest = models.CharField(max_length=255)
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    creator = models.ForeignKey(User, related_name="trips")
    deactivated = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="trips1")
    objects = TripManager()