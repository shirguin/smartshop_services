# Generated by Django 3.0.7 on 2020-07-04 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_auto_20200704_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='название')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='цена')),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orderapp.Phone', verbose_name='смартфон'),
        ),
    ]
