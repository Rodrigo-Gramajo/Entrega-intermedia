from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
   CATEGORIES = [
       ('Dulce', 'Dulce'),
       ('Salado', 'Salado'),
       ('Vegetariano', 'Vegetariano'),
       ('Desayunos', 'Desayunos'),
       ('Sopas', 'Sopas'),
   ]

   title = models.CharField(max_length=100)
   categoria = models.CharField(max_length=512, choices=CATEGORIES)
   ingredientes = models.TextField()
   description = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   image = models.ImageField( upload_to='files\archivos' ) 
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

def get_absolute_url(self):
      return reverse("recipes-detail", kwargs={"pk": self.pk})

def __str__(self):
    return self.title