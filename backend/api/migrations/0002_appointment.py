# Generated by Django 5.0.2 on 2024-02-17 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(max_length=255)),
                ('pet_name', models.CharField(max_length=255)),
                ('owner_name', models.CharField(max_length=255)),
                ('health_issue', models.CharField(max_length=255)),
                ('pet_gender', models.CharField(max_length=6)),
                ('appointment_date_time', models.DateTimeField()),
            ],
        ),
    ]
