from django.db import models

# Create your models here.


class Post(models.Model):
    s_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length = 30)
    content = models.TextField()
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by - " + self.author