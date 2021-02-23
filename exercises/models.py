from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self): 
        return self.name

class Exercise(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self): 
        return self.name
    
    
    def serialize(self):
        return {
           'id': self.id,
            'description': self.description,
            'name': self.name,
            'tags': self.tags.all()[0].name
        }
