# Generated by Django 3.2.3 on 2021-10-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
