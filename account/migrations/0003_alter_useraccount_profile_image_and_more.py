# Generated by Django 4.1.2 on 2022-10-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_useraccount_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.DeleteModel(
            name='AdditionalEmail',
        ),
    ]