from django.db import models

# Create your models here.
class Menus(models.Model):
	name = models.CharField(max_length=100)
	level = models.IntegerField()
