from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator


class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name

   
class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    content = models.TextField(null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='media', blank=True)
    slug = models.SlugField(unique = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topic_choices = [
      ('politique','Politique'),
      ('finance', 'Finance'),
      ('economique', 'Economique'),
      ('monde', 'Monde'),
      ('sport', 'Sport'),
      ('people', 'People'),
      ('santé', 'Sante'),
      ('actualité', 'Actualite'),
      ('international', 'International'),]
    topic = models.CharField(max_length=40,choices=topic_choices,default='Politique')
    
    def get_absolute_url(self):
        return reverse('lecambur:article_detail', kwargs={'slug':self.slug, 'pk':self.pk})
        
    def __str__(self):
        return self.title