# Generated by Django 4.1.7 on 2023-06-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_user_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='education',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='emailid',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.CharField(max_length=30),
        ),
    ]