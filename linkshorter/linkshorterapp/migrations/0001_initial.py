# Generated by Django 4.1.3 on 2022-11-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shorter',
            fields=[
                ('long_link', models.URLField(max_length=500)),
                ('short_link_hash', models.SlugField(max_length=7, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('days_alive', models.IntegerField(default=90)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
