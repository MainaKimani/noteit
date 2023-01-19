from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.decorators import api_view, permission_classes
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):

    #various routes together with their endpoints
    #this routes are used to query the database
    routes = [
       {
           'Endpoint': '/notes/',
           'method': 'GET',
           'body': None,
           'description': 'Returns an array of notes'
       },
       {
           'Endpoint': '/notes/id',
           'method': 'GET',
           'body': None,
           'description': 'Returns a single note object'
       },
       {
           'Endpoint': '/notes/create/',
           'method': 'POST',
           'body': {'body': ""},
           'description': 'Creates new note with data sent in post request'
       },
       {
           'Endpoint': '/notes/id/update/',
           'method': 'PUT',
           'body': {'body': ""},
           'description': 'Updates an existing note with data sent in post request'
       },
       {
           'Endpoint': '/notes/id/delete/',
           'method': 'DELETE',
           'body': None,
           'description': 'Deletes and exiting note'
       },
    ]
    return Response(routes)

class GetNotes(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = Note.objects.all().filter(owner=user.id).order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOwner])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    user = request.user
    data = request.data
    note = Note.objects.create(
        title=data['title'],
        body=data['body'],
        owner=user
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data=request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted successfully')
