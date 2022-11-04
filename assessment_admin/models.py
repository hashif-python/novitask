from django.db import models

# Create your models here.
class Products(models.Model):
    slno =models.CharField(max_length=255, null=True, blank=True)
    item_name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=255, null=True, blank=True)
    is_active =models.BooleanField(default=False)
    def __str__(self):
        return self.item_name