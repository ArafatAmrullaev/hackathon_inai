import os

from django.db import models

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.passport_id}.{ext}"
    return os.path.join("customers", new_filename)


class Customer(models.Model):
    passport_id = models.CharField(max_length=9, primary_key=True)
    pic = models.ImageField(upload_to=upload_to)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    inn = models.CharField(max_length=14)
    mkk = models.CharField(max_length=20)
    id_expire_date = models.DateField()
    id_recieved = models.DateField()
    vip_status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    

