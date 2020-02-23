from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
#for the post being posted on the blog
class Post(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
        ## after hitting the publish button it will look for post_detail
        ##page with the primary key pk of the same post

    def __str__(self):
        return self.title #will use reverse to get back to home page


class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=40)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
        #it will take to the list of blog post
        #

    def __str__(self):
        return self.text
