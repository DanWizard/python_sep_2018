from django.db import models
from django.core.validators import validate_email, ValidationError
import bcrypt


class UserManager(models.Manager):
	def validation(self, postdata):
		errors = {}

		if len(postdata['first_name']) < 2:
			errors['first_name'] = 'First name needs to be at least 2 characters.'
		if len(postdata['last_name']) < 2:
			errors['last_name'] = 'Last name needs to be at least 2 characters.'
		if len(postdata['password']) < 8:
			errors['password'] = 'password needs to be at least 8 characters.'
		try:
			validate_email(postdata['email'])
		except ValidationError as e:
			errors['email'] = 'invalid email format.'
		if postdata['password'] != postdata['passconfirm']:
			errors['password_confirm'] = 'passwords must match.'
		
		try:
			User.objects.get(email = postdata['email'])
			errors['email_taken'] = 'email has already been registered'
		except:
			print('success')


		return errors
	def login_validation(self,postdata):
		errors={}

		try:
			user = User.objects.get(email = postdata['username'])
			print('email')
			bcrypt.checkpw(postdata['pw'].encode(), user.password.encode())
			print('password')

		except Exception as e:
			errors['login'] = 'invalid login'
			print(e)
		return errors

class BookManager(models.Manager):
	def bookValidator(self,postdata):
		errors = {}

		if len(postdata['new_book']) < 1:
			errors['book'] = 'book cannot be empty'
		if len(postdata['new_author']) < 1 and not len(postdata['new_existing_author']):
				errors['author'] = 'must choose or create an author'
		if len(postdata['new_author']) > 1 and len(postdata['new_existing_author']) > 1:
			errors['authorTwo'] = 'can only choose one author entry option'
		try:
			Book.objects.get(author = postdata['new_author'])
			errors['authorThree'] = 'author already exists in the scroll down, cannot add again!'
		
		except Exception as e:
			print('passed')
			print(e)
		
		try:
			Book.objects.get(title = postdata['new_book'])
			errors['bookTwo'] = 'book already exists!'

		except Exception as e:
			print('also passed')
			print(e)


		return errors

class ReviewManager(models.Manager):
	def reviewValidator(self,postdata):
		errors = {}
		if len(postdata['new_review']) < 1:
			errors['review'] = 'review cannot be empty'
		return errors

class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	password = models.CharField(max_length = 255)
	objects = UserManager()

class Book(models.Model):
	user_who_uploaded = models.ForeignKey(User, related_name = 'user_books')
	title = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)
	rating = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()


class Review(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	review = models.TextField()
	review_from_user = models.ForeignKey(User, related_name = 'user_reviews')
	review_on_book = models.ForeignKey(Book, related_name = 'book_reviews')
	objects = ReviewManager()

