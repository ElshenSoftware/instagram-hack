from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(verbose_name='e-mailiniz')
    parol = models.CharField(max_length=20,verbose_name='parolunuz')
    ad = models.CharField(max_length=20)
    
