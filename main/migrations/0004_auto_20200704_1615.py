# Generated by Django 3.0.7 on 2020-07-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skill_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill_3',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
