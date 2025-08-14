from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView 
urlpatterns = [
    path("admin/", admin.site.urls),
   
    path("account/", include(("account.urls", "account"), namespace="account")),

    path("uçuşlar/", include(("uçuşlar.urls", "uçuşlar"), namespace="uçuşlar")),
    
    path("", RedirectView.as_view(pattern_name="account:main_page", permanent=False)),
]
