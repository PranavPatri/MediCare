# Generated by Django 5.0.2 on 2024-03-15 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.CharField(max_length=150),
        ),
    ]
