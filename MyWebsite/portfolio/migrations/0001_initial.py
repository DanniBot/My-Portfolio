# Generated by Django 3.2.5 on 2022-07-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=140)),
                ('image', models.ImageField(upload_to='MyWebsite/portfolio/images')),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]
