# Generated by Django 4.1.7 on 2023-06-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_register_education_alter_register_emailid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='emailid',
            field=models.EmailField(default='', max_length=30),
        ),
    ]