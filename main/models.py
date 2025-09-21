from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]