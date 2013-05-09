from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRIORITY_CHOICES = (
    (u'0', u'LOW'),
    (u'1', u'NORMAL'),
    (u'2', u'MEDIUM'),
    (u'3', u'HIGH'),
    )


CATEGORY_CHOICES = (
    (u'0', u'GENERAL'),
    (u'1', u'WORK'),
    (u'2', u'PERSONAL'),
    )


STATUS_CHOICES=(
    (u'0', u'NEW'),
    (u'1', u'DUE'),
    (u'2', u'PERSONAL'),
    )





class TodoItem(models.Model):
    user = models.ForeignKey(User)
    todo = models.TextField()
    priority = models.IntegerField(blank=True, null=True,choices=PRIORITY_CHOICES)
    created=models.DateTimeField()
    status=models.IntegerField(blank=True, null=True,choices=STATUS_CHOICES)
    category= models.IntegerField(blank=True, null=True,choices=CATEGORY_CHOICES)
    def __unicode__(self):
        if self.priority:
            return self.todo + " (priority: %s)" % self.priority
        else:
            return self.todo
    
