from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        # Length of name, Captial or not, no specail characters
        # email pattern, uniqu email
        # password length is greater than 8
        # password matchess confirm password
        if len(post_data['fname']) < 2:
            errors['fname'] = "First name must be at least 2 characters!"
        if len(post_data['lname']) < 2:
            errors['lname'] = "Last name must be at least 2 chracters!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Password must match"
        # Email pattern
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')          
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email_error'] = "Email isn't formatted correctly!"
        # Unique email
        user_list = User.objects.filter(email = post_data['email'])
        if len(user_list) > 0:
            errors['email'] = "Account already exists with email"    
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)    
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()