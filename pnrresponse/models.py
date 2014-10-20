from django.db import models

class PNRResponse(models.Model):
	pnr = models.IntegerField(max_length=10)
	boarding_point = models.CharField(max_length=3)
	reservation_upto = models.CharField(max_length=3)
	chart = models.BooleanField(default=False)
	cl = models.CharField(max_length=2)
	doj = models.DateField()
	frm = models.CharField(max_length=3)
	to = models.CharField(max_length=3)
	count = models.IntegerField(default=1)
	train_name = models.CharField(max_length=50)
	train_no = models.IntegerField()