# Generated by Django 4.1.7 on 2023-03-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('FULL TIME', 'Full Time'), ('PART TIME', 'Part Time'), ('DISTANCE', 'Distance')], max_length=30),
        ),
    ]
