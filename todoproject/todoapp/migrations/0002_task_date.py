# Generated by Django 4.2.1 on 2023-05-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-02-04'),
            preserve_default=False,
        ),
    ]
