# Generated by Django 4.2.7 on 2023-11-24 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('ochered', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='customers.customer'),
        ),
    ]
