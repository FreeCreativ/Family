# Generated by Django 4.0.5 on 2022-10-27 00:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('date_of_upload', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=datetime.datetime(2022, 10, 27, 0, 39, 53, 670416, tzinfo=utc), max_length=300, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('image_file', models.ImageField(upload_to='photos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_of_upload'],
                'abstract': False,
            },
            managers=[
                ('public', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ImageComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.image')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
                'abstract': False,
            },
        ),
    ]