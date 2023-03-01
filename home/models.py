from django.db import models
from django.utils import timezone

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=20, null=True)
    slug = models.SlugField(max_length=20, null=True)

    def __str__(self):
        return self.name
        


class Blog(models.Model):
    image = models.ImageField(upload_to="blogImages")
    title = models.CharField(max_length=100, verbose_name="Blog Title")
    summary = models.CharField(max_length=200, verbose_name="Blog Summary")
    text = models.TextField(verbose_name="Blog Text")
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)
    date = models.DateTimeField(default=timezone.now)
    categorys = models.ForeignKey(BlogCategory, null=True, on_delete=models.SET_NULL)


    # Admin panelinde listelenen objeler için tekil
    # eğer çoğul parametre eklemek istiyorsan dizindeki admin.py git (class BlogAdmin))
    def __str__(self):
        return self.title
