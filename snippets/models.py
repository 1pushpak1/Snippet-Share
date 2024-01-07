# snippets/models.py
from django.db import models

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField(default=10)  # Default snippet size

class SharedSnippet(models.Model):
    snippet = models.ForeignKey('Snippet', on_delete=models.CASCADE)
    visibility_expiry = models.DateTimeField()