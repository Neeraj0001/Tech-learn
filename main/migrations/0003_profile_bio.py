# Generated by Django 3.0.7 on 2020-07-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200703_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Bio',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
