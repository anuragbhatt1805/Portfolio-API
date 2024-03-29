# Generated by Django 4.2.9 on 2024-01-17 22:55

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=project.models.project)),
                ('repsitory', models.URLField()),
                ('url', models.URLField()),
                ('tags', models.ManyToManyField(to='certification.language')),
            ],
        ),
    ]
