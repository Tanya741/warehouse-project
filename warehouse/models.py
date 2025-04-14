from django.conf import settings
from django.db import models
from django.utils import timezone
from mongoengine import Document, StringField, IntField, DecimalField, DateTimeField, ReferenceField
from mongoengine import ValidationError


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

def validate_non_empty(value):
       if not value.strip():
        raise ValidationError("Brand must not be empty")

class Product(Document):
    name = StringField(max_length=70, required=True)
    description=StringField()
    category=StringField(maxlength=50)
    # category=ReferenceField('Category', required=False)
    price= DecimalField(precision=2, required=True)
    brand=StringField(max_length=70, required=True, validation=validate_non_empty)
    quantity=IntField()
    published_date=DateTimeField(default=None)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    

class Category(Document):
    title = StringField(max_length=50, required = True)
    description = StringField()
    published_date = DateTimeField(default=None)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_products(self):
        return Product.objects(category=self.title)
# Create your models here.
