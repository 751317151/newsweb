# Generated by Django 2.2.4 on 2019-10-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20191028_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sports',
            name='abs_titles',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='sports',
            name='imgurls',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='sports',
            name='titles',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='sports',
            name='urls',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
