from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Client, Festival, Template, Quotation
from .serializers import ClientSerializer, FestivalSerializer, TemplateSerializer, QuotationSerializer



class LoginView(APIView): 
    def post(self, request):
        print("Received request:", request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            print("User authenticated:", user.username)
            # JWT Token Generation
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Logged in successfully!'
            }, status=status.HTTP_200_OK)
        else:
            print("Authentication failed for:", username)
            return Response({'message': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)

        
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.AllowAny()]  # Allow all users to access GET requests
        return [permissions.IsAdminUser()]  # Only admins can create, update, or delete


class FestivalViewSet(viewsets.ModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]  # Only authenticated users can read
        return [permissions.IsAdminUser()]  # Only admins can create, update, or delete



class GreetingViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [permissions.IsAuthenticated]  # Users and admin both can read and create

    def perform_create(self, serializer):
        # Both users and admins can create greetings
        serializer.save()



class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]  #  users can read without authentication
        return [permissions.IsAdminUser()]  # Only admins can create, update, or delete

