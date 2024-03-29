# Generated by Django 3.0.6 on 2020-07-03 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Experience',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Internship',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
