# Generated by Django 4.2.1 on 2023-05-05 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('date_of_upload', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('movie_shot', models.ImageField(blank=True, upload_to='videoShots/2023-5-5/')),
                ('video_file', models.FileField(max_length=250, upload_to='videos/2023-5-5/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_of_upload'],
                'abstract': False,
            },
        ),
    ]
