# Generated by Django 2.2.5 on 2019-09-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineMarket', '0002_auto_20190920_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Other'), ('food', 'Food'), ('drink', 'Drink'), ('cloth', 'Cloth'), ('electronics', 'Electronics')], default='other', max_length=20, verbose_name='Category'),
        ),
    ]
