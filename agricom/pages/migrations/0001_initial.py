# Generated by Django 2.0.7 on 2018-11-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='Movers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('services', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Movers',
            },
        ),
    ]
