from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self,name):
        if name == '':
            raise serializers.ValidationError('El nombre no puede estar vacio')
        return name

    def validate(self, data):
        print ("verificando validaciones generales")

        return data