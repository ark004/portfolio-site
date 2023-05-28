from django.db import models




class face(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    urls = models.URLField()
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name