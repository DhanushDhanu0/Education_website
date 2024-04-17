from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=150)
    date = models.DateField(default=datetime.now(),blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
class loginData(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
          
      
    def __str__(self):
        return   self.username
    class Meta:
        verbose_name = 'loginData'
        verbose_name_plural = 'loginDatas'

    
    

