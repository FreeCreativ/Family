# Generated by Django 4.2.1 on 2023-05-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='images/2023-5-10/'),
        ),
    ]
