from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Post(models.Model):
    image=models.ImageField(upload_to = 'blog/',default='blog/default.jpg')
    auther=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category=models.ManyToManyField(Category)
    counted_view= models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    publish_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_date']
        #verbose_name='پست'
        #verbose_name_plural='پست ها'
    
    def __str__(self):
        return self.title
        
    def snippest(self):
        return self.content[:100]