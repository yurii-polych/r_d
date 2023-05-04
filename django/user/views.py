from user.models import User

from rest_framework.viewsets import ModelViewSet
from user.serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination


class UserPagination(PageNumberPagination):
    pass


class UserViewSet(ModelViewSet):
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = UserSerializer

    pagination_class = UserPagination
    UserPagination.page_size = 10
