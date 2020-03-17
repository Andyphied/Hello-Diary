from django.db import models

class Input(models.Model):
    text = models.TextField(blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)
    
