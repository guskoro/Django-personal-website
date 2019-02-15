from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    category = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, editable=False)
    email = models.EmailField(default='nama@gus.com')
    address = models.CharField(max_length=225,blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.title)