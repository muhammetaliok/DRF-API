from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note
from rest_framework import generics


@api_view(['GET',])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/eSecim/',
            'method': 'Get',
            'body': None,
            'description': 'Returns an array of notes' 
        },
        {
            'Endpoint': '/eSecim/id/',
            'method': 'Get',
            'body': None,
            'description': 'Returns a single note objects' 
        
        },
        {
            'Endpoint': '/eSecim/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post req' 
        },
        {
            'Endpoint': '/eSecim/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in' 
        },
        {
            'Endpoint': '/eSecim/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting note' 
        },
        
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteNote(request, pk):
    
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted!")

class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer