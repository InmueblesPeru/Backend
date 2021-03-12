# Generated by Django 3.1.6 on 2021-03-11 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.cities')),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.states'),
        ),
    ]
