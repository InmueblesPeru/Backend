# Generated by Django 3.1.6 on 2021-02-24 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210223_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type_user',
            field=models.IntegerField(choices=[(0, 'Unselected'), (1, 'Buyer'), (2, 'Seller')], default=0),
        ),
    ]