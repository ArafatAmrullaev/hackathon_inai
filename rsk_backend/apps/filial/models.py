from django.db import models

class Address(models.Model):
    ltd = models.CharField()
    lng = models.CharField()
    street_name = models.CharField()


class Filial(models.Model):
    address = models.OneToOneField(Address, related_name='filials', on_delete=models.CASCADE)
    name = models.CharField()


class Kassa(models.Model):
    filial = models.ForeignKey(Filial, related_name='filials', on_delete=models.CASCADE)
    number = models.IntegerField()
    is_operacionist = models.BooleanField()
    
