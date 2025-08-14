from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["flt_no", "sector", "sch_dep_dt", "sch_dep_tm"]
        widgets = {
            "flt_no": forms.TextInput(attrs={"class": "form-control"}),
            "sector": forms.TextInput(attrs={"class": "form-control"}),
            "sch_dep_dt": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "sch_dep_tm": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
        }

