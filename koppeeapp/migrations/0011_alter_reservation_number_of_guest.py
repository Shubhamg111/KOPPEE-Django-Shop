# Generated by Django 4.2.16 on 2024-10-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koppeeapp', '0010_client_remove_reservation_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number_of_guest',
            field=models.CharField(max_length=10),
        ),
    ]
