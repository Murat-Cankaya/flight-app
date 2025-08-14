from django.urls import path
from . import views
from django.urls import path
from .views import main_page

app_name = "uçuşlar"

urlpatterns = [
    path("", main_page, name="main_page"), 
]

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/ucak
# http://127.0.0.1:8000/ucak2
# http://127.0.0.1:8000/tokyo_ucusu


urlpatterns = [
    path("",views.ucak),
]

urlpatterns = [
    path("add/", views.flight_create, name="flight_add"),
    path("<int:pk>/edit/", views.flight_update, name="flight_edit"),
    path("<int:pk>/delete/", views.flight_delete, name="flight_delete"),
]