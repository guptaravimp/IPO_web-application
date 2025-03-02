# from django.db import models

# Create your models here.
from django.db import models
class IPOUpcoming(models.Model):
    icons = models.FileField(upload_to='home/', null=True, blank=True)
    company_name=models.CharField(max_length=100)
    company_link=models.URLField(max_length=200)
    price_band=models.CharField(max_length=50)
    open_date=models.DateField(auto_now_add=True)
    close_date=models.DateField(auto_now_add=True)
    issue_size=models.CharField(max_length=50)
    issue_type=models.CharField(max_length=50)
    listing_date=models.DateField(auto_now_add=True)

class FaqModel(models.Model):
    question=models.CharField(max_length=200)
    ans1=models.CharField(max_length=300)
    ans2=models.CharField(max_length=300)
    ans3=models.CharField(max_length=300)
    ans4=models.CharField(max_length=300)
    ans5=models.CharField(max_length=300)

class Broker(models.Model):
    icons = models.FileField(upload_to='home/', null=True, blank=True)
    company_name = models.CharField(max_length=100)
    rating = models.FloatField()
    Opening_charge = models.CharField(max_length=15)
    maintanance_charge = models.CharField(max_length=100, blank=True, null=True)
    percent_delivery_brokage = models.FloatField(max_length=50)
    percent_interaday_brokage = models.FloatField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)