# Generated by Django 4.2.1 on 2023-05-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='movie_shot',
            field=models.ImageField(blank=True, upload_to='videoShots/2023-5-10/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(max_length=250, upload_to='videos/2023-5-10/'),
        ),
    ]
