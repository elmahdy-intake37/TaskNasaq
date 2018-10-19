from django.db import models


# to run dummy data python manage.py load_random_task_data
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150, null=True)
    description = models.TextField(blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
