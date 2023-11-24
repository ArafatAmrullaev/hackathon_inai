from django.db import models

class Customer(models.Model):
    passport_id = models.CharField(max_length=9, primary_key=True)
    pic = models.ImageField(upload_to='customers')
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    inn = models.CharField(max_length=14)
    mkk = models.CharField(max_length=20)
    id_expire_date = models.DateField()
    id_recieved = models.DateField()
    vip_status = models.BooleanField()
    

