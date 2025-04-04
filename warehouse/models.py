from django.conf import settings
from django.db import models
from django.utils import timezone
from mongoengine import Document, StringField, IntField, DecimalField, DateTimeField

# class Product(models.Model):
#     name= models.CharField(max_length=70)
#     description= models.TextField()
#     category= models.CharField(max_length=100)
#     price= models.DecimalField(max_digits=10, decimal_places=2)
#     brand= models.CharField(max_length=70)
#     quantity= models.IntegerField()
#     published_date = models.DateTimeField(blank=True,  null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.name
    

class Product(Document):
    name = StringField(max_length=70, required=True)
    description=StringField()
    category=StringField(max_length=100)
    price= DecimalField(precision=2, required=True)
    brand=StringField(max_length=70)
    quantity=IntField()
    published_date=DateTimeField(default=None)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
# Create your models here.
