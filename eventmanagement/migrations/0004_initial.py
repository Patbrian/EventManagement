# Generated by Django 4.2.7 on 2024-04-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventmanagement', '0003_delete_event_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('organizer', models.CharField(max_length=100)),
                ('ticket_link', models.URLField()),
            ],
        ),
    ]
