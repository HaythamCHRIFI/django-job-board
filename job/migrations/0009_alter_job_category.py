# Generated by Django 4.1.7 on 2023-03-09 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
        ),
    ]
