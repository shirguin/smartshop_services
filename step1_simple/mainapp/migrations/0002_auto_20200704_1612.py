# Generated by Django 3.0.7 on 2020-07-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=16, unique=True, verbose_name='название'),
        ),
    ]
