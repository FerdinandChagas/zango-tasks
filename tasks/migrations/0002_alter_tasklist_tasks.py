# Generated by Django 4.0.10 on 2023-09-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='tasks',
            field=models.ManyToManyField(null=True, to='tasks.task'),
        ),
    ]
