from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('Examinations', 'Examinations'),
        ('Assignments & Projects', 'Assignments & Projects'),
        ('Workshops & Presentations', 'Workshops & Presentations'),
        ('School activities', 'School activities'),
        ('Holidays & Breaks', 'Holidays & Breaks'),
    ]
    
    event_id = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)

    def __str__(self):
        return self.title
