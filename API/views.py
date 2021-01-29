from .models import Note
from django.contrib.auth.models import User
from .serializers import UserSerializer, NoteSerializer

from django.http import JsonResponse #zwraca surowy obraz json w przeglądarce (wymaga parametru safe=False)
from rest_framework.response import Response #zwraca interfejs RestApi z json w przeglądarce
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def note_list(request):
    """func return full list of note"""
    user = request.user
    notes = Note.objects.filter(author=user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def users_list(request):
    """func return user list"""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def note_detail(request, pk):
    """func return single note by id(pk)"""
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)


@api_view(['POST'])
def note_create(request):
    """Func create new note. User need to provide title,
     content and author(id). Rest is default (position_top, position_left,
     color) but user can change this value."""

    try:
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except Exception:
        return Response("Something terrible went wrong. Can't create this note.")


@api_view(['POST'])
def note_update(request, pk):
    """Func will update selected by user note."""
    try:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except Exception:
        return Response("Something terrible went wrong. Can't update this note.")


@api_view(['DELETE'])
def note_delete(request, pk):
    try:
        note = Note.objects.get(id=pk)
        note.delete()
        return Response(f"Successful delete note {note.id}.")
    except Exception:
        return Response("Something terrible went wrong. Can't delete this note.")
