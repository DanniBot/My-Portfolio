# Generated by Django 3.2.5 on 2022-07-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_project_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ps',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
