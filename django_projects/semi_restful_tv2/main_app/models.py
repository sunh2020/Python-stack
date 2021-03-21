from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def validate_show(self, post_data):
        errors ={}
        if len(post_data['title']) < 2:
           errors['title'] = "Title must be longer than 2 characters"
        if len(post_data['network']) < 2:
           errors['network'] = "Network must be longer than 2 characters"
        if len(post_data['release_date']) < 2:
           errors['release_date'] = "Release Date must be longer than 2 characters"
        if len(post_data['description']) < 2:
           errors['description'] = "Description must be longer than 2 characters" 
        return errors

class User(models.Model):
   name = models.CharField(max_length=45)


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()

    creator = models.ForeignKey(User, related_name="shows_created", on_delete = models.CASCADE) 

    objects = ShowManager()
    #  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
