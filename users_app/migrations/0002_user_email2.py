# Generated by Django 3.2.1 on 2021-05-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email2',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
