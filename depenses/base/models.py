from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Access(models.Model):
    
    active = models.BooleanField(default = True)
    date = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length = 256)
    reason = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)
    details = models.TextField(blank = True)
    archived = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
    def __str__(self):
        return str(self.title) + " - " + self.date.strftime("%a %d %b %Y, %H:%M")

    class Meta():
        ordering = ['-date', '-updated_on']
