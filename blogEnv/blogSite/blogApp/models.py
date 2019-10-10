from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    published_time = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_time=timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey('blogApp.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=250)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def __str__(self):
        return self.author
