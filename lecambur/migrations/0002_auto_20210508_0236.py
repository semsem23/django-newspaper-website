# Generated by Django 2.2.5 on 2021-05-08 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecambur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
