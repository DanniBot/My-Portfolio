# Generated by Django 3.2.5 on 2022-07-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]