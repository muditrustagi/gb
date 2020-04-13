from django.db import models
import datetime

# Create your models here.
class Item(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField(max_length=100,default="")
	qty= models.CharField(max_length=100,default="")
	status= models.CharField(max_length=15,default="")
	date=  models.DateField(default=datetime.date.today)


