from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()


class Post(models.Model):
    object = models.Manager()
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=100, null=True, blank=True, unique=False)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return f"/blog/{self.id}/"

    def total_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "Profile of user {}".format(self.user.username)


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.post.title + " Image"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('Comment', null=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))
