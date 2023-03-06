from django.db import models
from django.db.models.fields import *
from django.db.models.fields.files import *

# Create your models here.

class Project(models.Model):
    title = CharField('Title', help_text='Title of the project', max_length=100)
    description = TextField('Information', help_text='Info about the project', max_length=300)
    image1 = ImageField('First image', help_text='Image of the project', upload_to='projects/')
    image2 = ImageField('Second image', help_text='Second image of the project', upload_to='projects/')
    date = DateField('Date', help_text='Finish date of the project')
    url = URLField('URL', help_text='URL of the project (GitHub or web link)', max_length=200)
    languages = TextField('Languages', help_text='Languages used to develop this project', max_length=150)
    counter = IntegerField('Counter of the project')
    
    def __str__(self):
        return f'Project {self.title}.'


