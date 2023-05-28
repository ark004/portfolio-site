from django.db import models




class face(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    urls = models.URLField()
    images = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name
    
class pdf(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')    
    def __str__(self):
        return self.pdf_file