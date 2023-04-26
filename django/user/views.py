from user.models import User
from user.forms import UserCreateForm

from django.views.generic import ListView, DetailView, CreateView


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = '/users'
