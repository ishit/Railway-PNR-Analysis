from django.db import models
from pnrresponse.models import PNRResponse

class Passenger(models.Model):
	response = models.ForeignKey(PNRResponse)
	booking_status = models.CharField(max_length=30)
	current_status = models.CharField(max_length=30)