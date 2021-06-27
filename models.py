from django.db import models

# Create your models here.


class Book(models.Model):
    college = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    year = models.CharField(max_length=5)
    semister = models.CharField(max_length=15)
    subject = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    cover_image = models.ImageField(upload_to='cover_images', verbose_name='Cover Image')
    notesfile = models.FileField(upload_to='downloads')

    def __str__(self):
        return self.college