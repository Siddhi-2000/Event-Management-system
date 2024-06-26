# Generated by Django 5.0.4 on 2024-05-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('rsvp_option', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('rsvp_option', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('rsvp_option', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('rsvp_option', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='CommunityMeetup',
        ),
    ]
