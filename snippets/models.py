from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, default='python')


    owner = models.ForeignKey(
        User, related_name='snippets', on_delete=models.CASCADE
    )
    highlighted = models.TextField(blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title