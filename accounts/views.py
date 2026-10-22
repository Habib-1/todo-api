from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

# Create your views here.


# class RegisterView(generics.CreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=RegisterSerializer
#     permission_classes=[AllowAny]

# class LogoutView(APIView):
#     permission_classes=[IsAuthenticated]

#     def post(self,request):
#         try:
#             refresh_token=request.data['refresh_token']
#             token=RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as error:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def RegisterView(request):

    serializer=RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def LogoutView(request):
   try:
        refresh_token=request.data["refresh_token"]
        token=RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
   except Exception as error:
        return Response({"stage": "token_validation", "detail": str(error)},status=status.HTTP_400_BAD_REQUEST)