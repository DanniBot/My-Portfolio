# Generated by Django 3.2.5 on 2022-07-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]