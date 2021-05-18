from django.db import models
import datetime
class Valid_Input(models.Manager):
    def base_valid(self, postData):
     
        errors = {}
        if len(postData['title_input']) < 2:
            errors['title_input'] = "Show Title must be 2 characters or more."
        if len(postData['network_input']) < 3:
            errors['network_input'] = "Network must be 3 characters or more."
        if len(postData['desc_input']) < 10:
            errors['desc_input'] = "Description must be 10 characters or more"
        return errors

class TV_Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField(default='01/01/2000')
    description = models.TextField(default='No description provided.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Valid_Input()