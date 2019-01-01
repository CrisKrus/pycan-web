# Generated by Django 2.1.2 on 2018-10-31 11:49

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_image', models.ImageField(upload_to='events/badges/')),
                ('name_coordinates', models.CharField(default='0,0', max_length=255, verbose_name='Person name coordinates (eg 15,23).')),
                ('name_font_size', models.PositiveIntegerField(default=24)),
                ('name_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('number_coordinates', models.CharField(default='0,0', max_length=255, verbose_name='Ticket number coordinates')),
                ('number_font_size', models.PositiveIntegerField(default=24)),
                ('number_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('category_coordinates', models.CharField(default='0,0', max_length=255, verbose_name='Ticket category coordinates')),
                ('category_font_size', models.PositiveIntegerField(default=24)),
                ('category_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]