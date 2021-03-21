from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors ={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')   
        if len(post_data['fname']) < 2:
            errors['fname_error'] = "First name must be at least 2 characters!!"
        if len(post_data['lname']) < 2:
            errors['lname_error'] = "Last name must be at least 2 chracters!!"
        if len(post_data['fav_color_error']) == 0:
            errors['fav_color_error'] = "No color given!"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email_error'] = "Email isn't formatted correctly!"
        return errors


class User(models.Model):
    fname = models.CharField(man_length=255)    
    lname = models.CharField(man_length=255)
    fav_color = models.CharField(man_length=255)
    email = models.CharField(man_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()