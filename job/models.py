from django.db import models

# Create your models here.
'''
django model filed:
    -html widget
    -validation
    -db size
'''
JOB_TYPE = (
    ('FULL TIME', 'Full Time'),
    ('PART TIME', 'Part Time'),
    ('DISTANCE', 'Distance'),
    )

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=30,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience_year = models.IntegerField(default=1)

    def __str__(self):
        return self.title

