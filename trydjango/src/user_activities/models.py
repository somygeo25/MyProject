from django.db import models

# Create your models here.

class ActivityPeriods(models.Model):
	user = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

	def __str__(self):
		return 'Activity {}'.format(self.id)

class Users(models.Model):
	AMERICA = 'AM'
	ASIA = 'AS'
	TIME_ZONE = (
		(AMERICA, 'America/Los_Angeles'),
		(ASIA, 'Asia/Kolkata'),
		
	)

	time_zone = models.CharField(max_length=2, choices=TIME_ZONE, default=AMERICA)
	real_name = models.CharField(max_length=20, verbose_name='name')

	def __str__(self):
		return self.real_name