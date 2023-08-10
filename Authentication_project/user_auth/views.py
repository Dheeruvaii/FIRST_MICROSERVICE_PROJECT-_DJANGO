from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
# from ...UserAuthenticationService.users.producer import publish
from .producer import publish

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # def get_authenticators(self):
    #     if self.action_map.get('put') or self.action_map.get('delete'):
    #         return [TokenAuthentication()]
    #     return super().get_authenticators()

    # def get_permissions(self):
    #     if self.action_map.get('put') or self.action_map.get('delete'):
    #         return [IsAuthenticated()]
    #     return super().get_permissions()

    def get_user_id_from_token(self, token):
        try:
            authentication = JWTAuthentication()
            validated_token = authentication.get_validated_token(token)
            user = authentication.get_user(validated_token)
            return user.id
        except TokenError:
            # Token is either expired or invalid
            return None

    def retrieve(self, request, *args, **kwargs):
        user_id_from_access_token = self.get_user_id_from_token(request.COOKIES.get('access_token'))
        if user_id_from_access_token:
            # Token is valid, get the user from the database
            try:
                user = User.objects.get(pk=user_id_from_access_token)
                serializer = self.get_serializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({"detail": "User not found."}, status=404)
        else:
            return Response({"detail": "Invalid or expired access token."}, status=401)

    # Add similar logic for other viewset actions like create, update, delete, etc.
    # Ensure that the access token is validated before performing any sensitive operations.


class UserLoginView(TokenObtainPairView):
    def post(self,request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data['access']
        refresh_token = response.data['refresh']
        token = RefreshToken(refresh_token)

        response =  Response({
            'access_token':access_token,
            'refresh_token':str(refresh_token),
            'id':token.payload['user_id'],
            'username':User.objects.get(id=token.payload['user_id']).username,
            'email': User.objects.get(id=token.payload['user_id']).email
        })

        # setting access and refresh token in cookie
        response.set_cookie('access_token',access_token, httponly=True)
        response.set_cookie('refresh_token',refresh_token, httponly=True)
        return response
    

class FavoriteProductViewSet(ViewSet):
    def create(self, request):
        serializer = FavoriteProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data['user_id']  # Temporarily using a fixed user ID for testing
        product_id = serializer.validated_data['product_id']

        # Publish the message to RabbitMQ
        publish(user_id, product_id)

        return Response({'message': 'Favorite product request sent'})


# class FavProductsViewSet(ModelViewSet):
#     queryset = FavProducts.objects.all()
#     serializer_class = FavoriteProductsSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return FavProducts.objects.filter(user=self.request.user)
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)

    #     user_id = '1'  #PAXI JWT DECODE GARERA YESMA ID HALNI
    #     product_id = response.data.get('id')  

    #     # Publish the message to RabbitMQ
    #     publish(user_id, product_id)

    #     return response

    


        
             