import email
from email.policy import default
from tkinter import N
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50, default="", blank=True, null=True)
    user=models.ForeignKey('user.CustomUser',on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return str(self.id)



# class Tag(models.Model):
#     tag_name = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.tag_name)



class Blog(models.Model):
    user_name=models.ForeignKey('user.CustomUser',on_delete=models.CASCADE, default=None)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    
   

    title=models.CharField(max_length=100, default="")
    thought=models.TextField( default="")

    desc=HTMLField()
    desc1=HTMLField(default="")

    date=models.DateTimeField(auto_now_add=True, null=True)
    liked=models.ManyToManyField('user.CustomUser', default=None, blank=True, related_name='liked')
    total_like = models.IntegerField(default=0,blank=True,null=True)

    # tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    image = models.ImageField( upload_to='image/', default="")
    # image = models.CharField(max_length=100, default="",blank=True,null=True)
    # image1 = models.ImageField( upload_to='image/', default="")

    v = models.IntegerField(default=0 ,blank=True, null=True)
    mobile_view = models.IntegerField(default=0 ,blank=True, null=True)
    desktop_view = models.IntegerField(default=0 ,blank=True, null=True)
    tablet_view = models.IntegerField(default=0 ,blank=True, null=True)
    s_view = models.IntegerField(default=0 ,blank=True, null=True)


    # status = models.BooleanField(default=False)

    date_added = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return str(self.id)
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
    # def get_absolute_url(self):
    #     return reverse('blog',kwargs={'pk':self.pk})
    

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, default="")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, default=True, related_name='blog')
    value=models.CharField(choices=LIKE_CHOICES,max_length=50,default='Like')
    
    def __str__(self):
        return str(self.blog)
    
    
class Comment(models.Model):
        
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, blank=True, default=True)
    content = models.TextField()
    email=models.EmailField( max_length=254, default="" , null=True)
    website = models.CharField( max_length=50, default="" , null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name="comments", blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.id)


class Contact(models.Model):
        
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, blank=True, default=True)
    content = models.TextField()
    email=models.EmailField( max_length=254, default="" , null=True)
    website = models.CharField( max_length=50, default="" , null=True)
   
    
    def __str__(self):
        return str(self.id)


class Quote(models.Model):
    q = models.TextField()

    def __str__(self):
        return str(self.q)


class Replycomment(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, blank=True, default=True,null=True)
    reply_body = models.TextField(default="")
    comment= models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.id)





GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

# SOCIALMEDIA_CHOICES = (
#     ('Facebook', 'Facebook'),
#     ('Twitter', 'Twitter'),
#     ('Instagram', 'Instagram'),

# )

class Profile(models.Model):
    username = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, blank=True, default=True, unique=False)
    fname=models.CharField( max_length=254, default="" , null=True)
    lname=models.CharField( max_length=254, default="" , null=True)
    city=models.CharField( max_length=254, default="" , null=True)
    address=models.CharField( max_length=254, default="" , null=True)
    country=models.CharField( max_length=254, default="" , null=True)
    about_me=models.CharField( max_length=254, default="" , null=True)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=50,default='')
    skill=models.CharField( max_length=254, default="" , null=True)
    dob=models.DateField(default=datetime.now)
    facebook=models.CharField( max_length=254, default="" , null=True)
    twitter=models.CharField( max_length=254, default="" , null=True)
    instagram=models.CharField( max_length=254, default="" , null=True)
    whatsapp=models.CharField( max_length=254, default="" , null=True)
    gmail=models.CharField( max_length=254, default="" , null=True)
    reddit=models.CharField( max_length=254, default="" , null=True)

    website=models.CharField( max_length=254, default="" , null=True)
    image=models.CharField( max_length=254, default="" , null=True)
    follow=models.IntegerField(default=0 ,blank=True, null=True)
    following=models.IntegerField(default=0 ,blank=True, null=True)

def __str__(self):
        return str(self.fname)



