from django.db import models


class Topic(models.Model):
    category = models.TextField()
    source = models.TextField()
    target = models.TextField()
    pic = models.TextField()

    def __unicode__(self):
        return self.category


class Item(models.Model):
    topic = models.ForeignKey(Topic)
    category = models.TextField()
    source = models.TextField()
    target = models.TextField()

    def __unicode__(self):
        return self.source
