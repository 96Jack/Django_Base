from pyexpat import model
from django.db import models

# Create your models here.
 
class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)

    class Meta:
        db_table = 'person'

    @classmethod
    def create(cls, name, age):
        return cls(name=name, age=age)