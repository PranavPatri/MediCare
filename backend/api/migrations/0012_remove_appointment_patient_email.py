# Generated by Django 5.0.2 on 2024-03-16 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_appointment_patient_email_alter_pet_ownermail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient_email',
        ),
    ]