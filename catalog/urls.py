from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/create/", views.UserView.as_view(), name="create"),
    path("user/auth/", include("rest_framework.urls")),
    path("hotels/", views.HotelListView.as_view(), name="hotel-list"),
]
