from django.db import models


class Topic(models.Model):
    """A topic the user is journaling about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __string__(self):
        """Define a string representation of the string."""
        return self.text
