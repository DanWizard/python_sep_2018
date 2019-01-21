from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
import bcrypt



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
	'recent_book_review' :Book.objects.all().order_by('id')[:3],
	'all_books_with_reviews': Book.objects.all()
	}
	print(context)
	return render(request, 'first_app/home.html', context)

def displayAddReview(request):
	context = {
	'authors': Book.objects.all()
	}
	print(context['authors'])
	return render(request, 'first_app/addBook.html', context)

def logoff(request):
	request.session.clear()
	return redirect('/')

def processBnR(request):
	errorsB = Book.objects.bookValidator(request.POST)
	errorsR = Review.objects.reviewValidator(request.POST)

	if len(errorsB) or len(errorsR):
		for keys, value in errorsR.items():
			messages.error(request, value, extra_tags = 'msgs')
		for keys, value in errorsB.items():
			messages.error(request, value, extra_tags = 'msgs')
		return redirect('/displayAdd')

	else:
		Book.objects.create(title = request.POST['new_book'], author = request.POST['new_author'], user_who_uploaded_id = request.session['user_id'], rating = request.POST['rating'])
		Review.objects.create(review = request.POST['new_review'], review_from_user_id = request.session['user_id'], review_on_book = Book.objects.last())
	return redirect('/home')

def bookInfo(request, id):
	context = {
	'book_data' : Book.objects.get(id = id)
	}
	return render(request, 'first_app/bookInfo.html', context )

def processR(request, id):
	errors = Review.objects.reviewValidator(request.POST)
	if len(errors):
		for keys, value in errors.items():
			messages.error(request, value, extra_tags='msgs')

		return redirect('/home')
	else:
		Review.objects.create(review = request.POST['new_review'], review_from_user_id = request.session['user_id'], review_on_book = Book.objects.get(id = request.POST['redirect']))
		return redirect('/home')

def userInfo(request, id):
	context = {
	'user_reviews' : User.objects.get(id = id)
	}
	return render(request, 'first_app/userReviews.html', context)


