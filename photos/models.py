from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()
