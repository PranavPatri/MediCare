# Generated by Django 5.0.2 on 2024-02-17 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='petmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='pets',
            name='petid',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
