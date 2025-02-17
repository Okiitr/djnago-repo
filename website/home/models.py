from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.UUIDField(primary_key=True,unique=True)
    name = models.CharField(max_length=100,null=False,blank=False)
    desc = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qantity = models.IntegerField(null=True,blank=True)
    
    class Meta:
        db_table = "products"
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    