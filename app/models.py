from django.db import models

# Create your models here.
class user_inform(models.Model):
    fname = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False)
    subject = models.TextField(max_length=220, blank=False)
    message = models.TextField(max_length=400, blank=False)


    def __str__(self):
        return f"a message by {self.fname} "