# Generated by Django 4.1.3 on 2023-01-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0013_alter_video_movie_shot_alter_video_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='movie_shot',
            field=models.ImageField(blank=True, upload_to='movieShot/2023-1-4/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='video/2023-1-4/'),
        ),
    ]