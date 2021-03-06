# Generated by Django 3.0.8 on 2020-07-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('middleName', models.TextField()),
                ('lastName', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('pcost', models.FloatField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('idClient', models.ManyToManyField(to='inventory.clients')),
            ],
        ),
        migrations.CreateModel(
            name='servicing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('idClient', models.ManyToManyField(to='inventory.clients')),
                ('idSale', models.ManyToManyField(to='inventory.sales')),
            ],
        ),
        migrations.CreateModel(
            name='sales_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.TextField()),
                ('expenses', models.FloatField()),
                ('utility', models.FloatField()),
                ('idProduct', models.ManyToManyField(to='inventory.products')),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='idDetail',
            field=models.ManyToManyField(to='inventory.sales_detail'),
        ),
    ]
