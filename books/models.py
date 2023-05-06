from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    def __str__(self):
	    return u'%s %s' % (self.first_name, self.last_name)
	    #return self.first_name 
class Book(models.Model):
    authors=models.ManyToManyField(Author)
    title=models.CharField(max_length=70)
    content=models.CharField(max_length=150)
    publication=models.SmallIntegerField()
    num=models.SmallIntegerField()
    def __str__(self):
	    return self.title
class Hist(models.Model):
    ind=models.SmallIntegerField(default=0)
    title=models.CharField(max_length=70)
    content=models.TextField()
    image=models.ImageField(upload_to="bks/list",
          verbose_name="Основное изображение",null=True,blank=True)
    def __str__(self):
	    return self.title
class Artc(models.Model):
    ind=models.SmallIntegerField(default=0)
    title=models.CharField(max_length=70)
    content=models.TextField()
    image=models.ImageField(upload_to="bks/list",
          verbose_name="Основное изображение",null=True,blank=True)
    def __str__(self):
	    return self.title
class Dict(models.Model):
    lat=models.CharField(max_length=70)
    trans=models.CharField(max_length=70)
    rus=models.CharField(max_length=150)
    def __str__(self):
	    return self.lat
class Pros(models.Model):
    ind=models.SmallIntegerField(default=0)
    author=models.CharField(max_length=70)
    title=models.CharField(max_length=70)
    image=models.ImageField(upload_to="bks/list",
          verbose_name="Основное изображение",null=True,blank=True)
    def __str__(self):
	    return self.title		
		
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to="images",default="default/user.png")
    
    
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")
    
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")