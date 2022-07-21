from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return Response(user_serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
def user_decorator_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)

        return Response(user_serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def user_detail_view(request, pk = None):

    if request.method == 'GET':
        if pk is not None:
            user = User.objects.filter(id = pk).first()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        else:
            print("pk vacio")

    elif request.method == 'PUT':
        if pk is not None:
            user= User.objects.filter(id = pk).first()
            user_serializer = UserSerializer(user, data = request.data)
            if UserSerializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_202_ACCEPTED)
            return Response(user_serializer.errors)

    elif request.method == 'DELETE':
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response('usuario id = {} fue elemininado '.format(pk), status = status.HTTP_202_ACCEPTED)
