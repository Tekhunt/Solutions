# Generated by Django 3.2.9 on 2022-02-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_city', '0009_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=50, null=True),
        ),
    ]