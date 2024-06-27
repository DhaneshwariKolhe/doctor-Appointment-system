# Generated by Django 5.0.6 on 2024-06-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoravailability',
            name='day_of_wk',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thr', 'Thrusday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], default='Mon', max_length=10, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
