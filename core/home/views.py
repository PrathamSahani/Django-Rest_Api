from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import People
from .serializers import PersonSerializer

@api_view(['GET'])
def get_persons(request):
    persons = People.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response({
        'status': 200,
        'data': serializer.data
    })

@api_view(['POST'])
def save_person(request):
    data = request.data
    serializer = PersonSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'Data saved'
        })
    
    return Response({
        'status': 400,
        'message': 'something went wrong', 
        'data': serializer.errors
    })
