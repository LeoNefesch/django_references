# Generated by Django 3.2 on 2022-03-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_login', '0003_remove_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.TextField(max_length=20),
        ),
    ]
