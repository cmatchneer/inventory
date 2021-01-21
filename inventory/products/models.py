from django.db import models

# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank =True, null =True, default='test')
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity= models.IntegerField(default=0) 
    available = models.BooleanField(default=True)
    date = models.DateField(auto_now=False,auto_now_add=False, default="2021-11-1")

    # def get_absolute_url(self):
    #     return reverse("product:product-detail", kwargs={"id": self.id})