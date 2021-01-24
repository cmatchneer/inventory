from django.db import models
import datetime


# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255,blank =True, null =True, default='test')
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity= models.IntegerField(default=0) 
    available = models.BooleanField(default=True)
    date = models.DateField(auto_now=False,auto_now_add=False, default= datetime.date.today)

    