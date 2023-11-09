from django.db import models

class User(models.Model):
    mobile = models.CharField(max_length=10)
    
    def __str__(self):
        return self.mobile