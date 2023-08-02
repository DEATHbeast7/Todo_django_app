from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
class Category(models.Model) :
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProjectStatus(models.IntegerChoices):
    PENDING = 1, 'pending'
    COMPLETED = 2, 'completed'
    POSTPONED = 3, 'postponed'
    CANCELED =4, 'canceled'



class Projects(models.Model) :
    title = models.CharField(max_length=255)
    status = models.IntegerField(
        ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title


class Task(models.Model) :
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.description