from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from .models import Airline, Aircraft
from .serializers import AirlineSerializer, AircraftSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


# Token almak için kullanılan view
class TestTokenView(TokenObtainPairView):
    pass

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'username': user.username,
                    'email': user.email,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView kullanarak Airline işlemleri yapıldı
class AirlineListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AirlineRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            airline = Airline.objects.get(pk=pk)
        except Airline.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AirlineSerializer(airline)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            airline = Airline.objects.get(pk=pk)
        except Airline.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AirlineSerializer(airline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            airline = Airline.objects.get(pk=pk)
        except Airline.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AirlineSerializer(airline, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_airline(request):
    data = JSONParser().parse(request)
    pk = data.get('pk')
    
    try:
        airline = Airline.objects.get(pk=pk)
        airline.delete()
        return JsonResponse({'message': 'Airline deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Airline.DoesNotExist:
        return JsonResponse({'error': 'Airline not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def delete_aircraft(request):
    data = JSONParser().parse(request)
    pk = data.get('pk')
    
    try:
        aircraft = Aircraft.objects.get(pk=pk)
        aircraft.delete()
        return JsonResponse({'message': 'Aircraft deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Aircraft.DoesNotExist:
        return JsonResponse({'error': 'Aircraft not found'}, status=status.HTTP_404_NOT_FOUND)

# APIView Kullanarak Aircraft işlemleri yapıldı
class AircraftListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        aircrafts = Aircraft.objects.all()
        serializer = AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AircraftRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            aircraft = Aircraft.objects.get(pk=pk)
        except Aircraft.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            aircraft = Aircraft.objects.get(pk=pk)
        except Aircraft.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AircraftSerializer(aircraft, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            aircraft = Aircraft.objects.get(pk=pk)
        except Aircraft.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AircraftSerializer(aircraft, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
