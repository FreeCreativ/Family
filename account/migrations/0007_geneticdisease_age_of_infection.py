# Generated by Django 4.0.5 on 2022-07-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_geneticdisease_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='geneticdisease',
            name='age_of_infection',
            field=models.IntegerField(default=40, verbose_name='age of infection'),
            preserve_default=False,
        ),
    ]