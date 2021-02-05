from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="nazwa")
    content = models.TextField(blank=False, default="telefon1234")
    position_top = models.IntegerField(default=30)
    position_left = models.IntegerField(default=50)
    note_box_color = models.CharField(max_length=25, default="220, 220, 220")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, (created by: {self.author})'
