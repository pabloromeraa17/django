# Generated by Django 4.1 on 2022-08-31 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
