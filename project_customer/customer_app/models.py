from django.db import models
from django.contrib import admin
# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length=20, help_text="Enter customer Name")
    age = models.IntegerField(help_text="Enter age between 18 to 22")
    dob = models.DateField()
    customer_no = models.IntegerField(help_text="Enter the customer Number")

class customerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'age', 'dob', 'customer_no']
