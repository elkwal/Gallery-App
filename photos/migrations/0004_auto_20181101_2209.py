# Generated by Django 2.0 on 2018-11-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
