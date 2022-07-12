# Generated by Django 4.0.6 on 2022-07-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='')),
                ('weather_discription', models.IntegerField(choices=[(0, 'Sunny'), (1, 'Rain'), (2, 'Cloudy'), (3, 'Snow'), (4, 'Shady'), (5, 'Windy')], default=0)),
                ('coordinate', models.FloatField()),
                ('temp', models.FloatField(verbose_name='C')),
                ('humidity', models.IntegerField(verbose_name='')),
                ('windspeed', models.IntegerField(verbose_name='')),
                ('country', models.CharField(max_length=100, verbose_name='')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='')),
            ],
        ),
    ]