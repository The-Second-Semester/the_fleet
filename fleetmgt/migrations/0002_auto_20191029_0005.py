# Generated by Django 2.2.6 on 2019-10-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetmgt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fleetVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_no', models.CharField(max_length=30)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('colour', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
