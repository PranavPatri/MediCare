# Generated by Django 4.1.2 on 2024-02-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('petid', models.IntegerField(primary_key=True, serialize=False)),
                ('petname', models.CharField(max_length=100)),
                ('petgender', models.CharField(max_length=100)),
                ('petage', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]