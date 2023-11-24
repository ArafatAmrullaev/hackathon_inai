# Generated by Django 4.2.7 on 2023-11-24 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('filial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appointment_start', models.DateTimeField(null=True)),
                ('serviced_at', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='customers.customer')),
                ('kassa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='filial.kassa')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='ochered.operation')),
            ],
        ),
    ]