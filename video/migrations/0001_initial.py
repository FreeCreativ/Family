# Generated by Django 4.0.5 on 2022-07-06 18:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_upload', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=datetime.datetime(2022, 7, 6, 18, 38, 42, 336980, tzinfo=utc), max_length=300)),
                ('description', models.TextField()),
                ('public', models.BooleanField(default=True)),
                ('video_file', models.FileField(upload_to='videoF/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_of_upload'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video')),
            ],
            options={
                'ordering': ['date_created'],
                'abstract': False,
            },
        ),
    ]