from random import choices
from django.db import models
from django.forms import URLField
import django_filters

# Create your models here.
DJANGO = 'DJ'
PYTHON = 'Py'
RUST = 'Ru'
MACHINELEARNING = 'ML'
PUBLICATIONS = 'PB'
FLASK = 'FL'
TOPIC_CHOICES = (
    (DJANGO, 'Django'),
    (PYTHON, 'Python'),
    (FLASK, 'Flask'),
    (RUST, 'Rust'),
    (MACHINELEARNING, 'Machine Learning'),
    (PUBLICATIONS, 'Publications'),
)

class Project(models.Model):
    
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    topic=models.CharField(max_length=2,choices=TOPIC_CHOICES,default=PYTHON)
    image=models.ImageField(upload_to='portfolio/images/')
    link=models.URLField(blank=True)
    priority=models.IntegerField()
    ps=models.CharField(max_length=5,null=True,blank=True)
    
    def __str__(self):
        return self.title

class ProjectFilter(django_filters.FilterSet):
    topic=django_filters.ChoiceFilter(choices=TOPIC_CHOICES)
    class Meta:
        model=Project
        fields=['topic']