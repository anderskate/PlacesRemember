# Generated by Django 2.2.7 on 2019-11-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visited_places_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]
