# Generated by Django 3.1.4 on 2021-02-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_recurring',
            field=models.BooleanField(default=False),
        ),
    ]
