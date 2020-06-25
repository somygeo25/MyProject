# from django.db import models
# # from timezone_field import TimeZoneField
# # Create your models here.

# class ActivityPeriods(models.Model):
# 	start_time = models.DateTimeField()
# 	end_time = models.DateTimeField()

# # class Products(models.Model):
# # 	title = models.TextField()
# # 	description = models.TextField()
# # 	price = models.TextField()
# # 	activity = models.ForeignKey(ActivityPeriods, models.SET_NULL, null=True)

# class Users(models.Model):
# 	AMERICA = 'AM'
# 	ASIA = 'AS'
# 	TIME_ZONE = (
# 		(AMERICA, 'America/Los_Angeles'),
# 		(ASIA, 'Asia/Kolkata'),
		
# 	)
# 	time_zone = models.CharField(max_length=2, choices=TIME_ZONE, default=AMERICA)
# 	real_name = models.CharField(max_length=20)
# 	activity = models.ManyToManyField(ActivityPeriods, blank=True,related_name="activity_rec",related_query_name="activity")

# 	def __str__(self):
# 		return self.name