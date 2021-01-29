from django.contrib.auth.models import User
from .models import Note
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'author',
            'title',
            'content',
            'position_top',
            'position_left',
            'note_box_color',
            'create_date',
        )
