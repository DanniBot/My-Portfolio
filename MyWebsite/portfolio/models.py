from django.db import models
from django.forms import URLField

# Create your models here.
class Project(models.Model):
    DJANGO = 'DJ'
    PYTHON = 'Py'
    RUST = 'Ru'
    MACHINELEARNING = 'ML'
    PUBLICATIONS = 'PB'
    FLASK = 'FL'
    TOPIC_CHOICES = [
        (DJANGO, 'Django'),
        (PYTHON, 'Python'),
        (FLASK, 'Flask'),
        (RUST, 'Rust'),
        (MACHINELEARNING, 'Machine Learning'),
        (PUBLICATIONS, 'Publications'),
    ]
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    topic=models.CharField(max_length=2,choices=TOPIC_CHOICES,default=PYTHON)
    image=models.ImageField(upload_to='portfolio/images/')
    link=models.URLField(blank=True)
    
    def __str__(self):
        return self.title