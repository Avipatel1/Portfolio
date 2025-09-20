from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title