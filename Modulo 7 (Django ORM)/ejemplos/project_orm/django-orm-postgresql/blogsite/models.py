from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from  django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255) # Slug es un string que se puede convertir en una URL. Es único.
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    def get_absoulte_url(self): # Convierte slugs en cadenas
        return reverse('blog_post_detail', args=[self.slug]) 
    
    def save(self, *args, **kwargs): # Convierte cadenas en slugs. Guarda el slug para convertirlon en URL.
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title
        