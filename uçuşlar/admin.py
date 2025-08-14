from django.contrib import admin

from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("flt_no", "sector", "sch_dep_dt", "sch_dep_tm")  
    search_fields = ("flt_no", "sector") 
    list_filter = ("sch_dep_dt",)  

