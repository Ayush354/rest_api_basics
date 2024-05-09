from django.db import models

class ScrapeResult(models.Model):
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)

class Employee(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    sal = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return str(self.id)
    
class Student(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return str(self.id)
    

class Passenger(models.Model):
    id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    travelpoints = models.IntegerField()

    def __str__(self):
        return str(self.id)