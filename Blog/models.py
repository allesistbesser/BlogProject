from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
STATUS = [
    ('draft', 'Draft'),
    ('published', 'Published'),
   ]

class Post(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE )
    category = models.ForeignKey(Category , related_name='post', on_delete=models.PROTECT ) # Cascade yerine PROTECT olamsi lazim
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    image = models.URLField(max_length=1000, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10 , choices=STATUS)
    slug = models.SlugField(blank=True) # unige=True eklememiz gerekiyor
    
    def __str__(self):
        return self.title
    
    @property 
    def comment_count(self):
        return self.comment_set.count()
    
    @property 
    def like_count(self):
        return self.like_set.count()
    @property 
    def postview_count(self):
        return self.postview_set.count()
    
    
    
        
class Proflie(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_image = models.URLField(max_length=1000)
    bio = models.CharField(max_length=250)
    
    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)
    
    def __str__(self):
        return f'commentator {self.user} - post {self.post}'  

    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.title
    
               
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.title



      
     