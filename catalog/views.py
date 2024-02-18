from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


# Create your views here.
def index(request):
    return HttpResponse("Api index.")


class UserView(CreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
