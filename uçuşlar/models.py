from django.db import models
from django.db import models

class Flight(models.Model):
    flt_no = models.CharField(max_length=10)
    sector = models.CharField(max_length=10)      
    sch_dep_dt = models.DateField(max_length=100)
    sch_dep_tm = models.TimeField(max_length=120) 

    @property
    def origin(self):
        return self.sector[:3]

    @property
    def destination(self):
        return self.sector[3:]

    def __str__(self):
        return f"{self.flt_no} {self.origin}->{self.destination}"

