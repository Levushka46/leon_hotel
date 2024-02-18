from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import UserSerializer, HotelSerializer
from .models import User, Hotel


# Create your views here.
def index(request):
    return HttpResponse("Api index.")


class UserView(CreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class HotelListView(ListAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        queryset = Hotel.objects.all()
        city_id = self.request.query_params.get("city_id", None)
        from_id = self.request.query_params.get("from_id", None)
        limit = self.request.query_params.get("limit", None)

        if city_id:
            queryset = queryset.filter(city_id=city_id)

        if from_id:
            queryset = queryset.filter(id__gt=from_id)

        if limit:
            queryset = queryset[: int(limit)]

        return queryset
