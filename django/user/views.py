from user.models import User

from rest_framework.viewsets import ModelViewSet
from user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer