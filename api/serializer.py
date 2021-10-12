from rest_framework.serializers import ModelSerializer
from .models import User, Image

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
