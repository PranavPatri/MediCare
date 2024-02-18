# Generated by Django 5.0.2 on 2024-02-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pets_petmail_alter_pets_petid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('petid', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('ownermail', models.EmailField(max_length=254)),
                ('petname', models.CharField(max_length=100)),
                ('petgender', models.CharField(max_length=100)),
                ('petage', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Pets',
        ),
    ]