# Generated by Django 4.0.5 on 2022-06-23 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_education_school_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='dad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father', to='account.userdetail'),
        ),
        migrations.AlterField(
            model_name='education',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]