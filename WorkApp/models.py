from django.db import models

# Create your models here.

class Personal(models.Model):
	Alastname = models.TextField(default="")
	Afirstname = models.TextField(default="")
	Amiddlename = models.TextField(default="")
	Abday = models.TextField(default="")
	Aemailadd = models.TextField(default="")
	Acontactnum = models.TextField(default="")