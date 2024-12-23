from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name




    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class Proffesionalchef(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    maqom = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Staywithus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    day = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Ourgallery(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image.url) 
    
class Contact(models.Model):
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    openinghours = models.TimeField()


    def __str__(self):
        return self.address
    
