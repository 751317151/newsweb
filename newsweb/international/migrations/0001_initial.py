# Generated by Django 2.2.4 on 2019-11-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='international',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(default=0, max_length=255)),
                ('urls', models.CharField(default=0, max_length=255)),
                ('abs_titles', models.CharField(default=0, max_length=255)),
                ('imgurls', models.CharField(default=0, max_length=255)),
            ],
        ),
    ]
