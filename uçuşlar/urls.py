from django.urls import path
from . import views
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/ucak
# http://127.0.0.1:8000/ucak2
# http://127.0.0.1:8000/tokyo_ucusu


urlpatterns = [
    path("",views.ucak),
]
