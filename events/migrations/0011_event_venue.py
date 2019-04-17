# Generated by Django 2.1.4 on 2019-04-17 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20180827_1816'),
        ('events', '0010_auto_20190319_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='events', to='locations.Venue'),
        ),
    ]
