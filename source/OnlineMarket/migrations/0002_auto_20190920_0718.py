# Generated by Django 2.2.5 on 2019-09-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineMarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
