from django.db import models
import re
from django.db.models.deletion import CASCADE

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        if len(post_data['fname']) < 2:
            errors['fname'] = "First name must be at least 2 characters!"
        if len(post_data['lname']) < 2:
            errors['lname'] = "Last name must be at least 2 chracters!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Password must match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')          
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email_error'] = "Email isn't formatted correctly!"
        user_list = User.objects.filter(email = post_data['email'])
        if len(user_list) > 0:
            errors['email'] = "Account already exists with email"    
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def book_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 1:
            errors['title'] = "Title must be provided!"
        if len(post_data['description']) < 5:
            errors['description'] = "Description must be at least 5 characters!"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()