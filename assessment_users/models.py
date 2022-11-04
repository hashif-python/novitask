from django.db import models
from django.contrib.auth.models import User
from assessment_admin.models import *
# Create your models here.
class UserCart(models.Model):
	customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	amount = models.CharField(max_length=200, null=True)
	total = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.customer.username