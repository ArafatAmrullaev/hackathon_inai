from django.db import models
from django.utils.text import slugify


class Address(models.Model):
    ltd = models.CharField()
    lng = models.CharField()
    street_name = models.CharField(max_length=255)


class Filial(models.Model):
    slug = models.SlugField(primary_key=True, unique=True)
    address = models.OneToOneField(Address, related_name='filials', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Kassa(models.Model):
    slug = models.SlugField(primary_key=True, unique=True)
    filial = models.ForeignKey(Filial, related_name='filials', on_delete=models.CASCADE)
    number = models.IntegerField()
    is_operacionist = models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(f'{self.filial.slug} kassa {self.number}')
        super().save(*args, **kwargs)

