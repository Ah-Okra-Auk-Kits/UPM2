# Generated by Django 3.2.18 on 2023-03-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]