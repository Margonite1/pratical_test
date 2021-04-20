from django.db import models

class News_Item(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.title

