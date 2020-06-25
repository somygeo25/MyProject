from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import JsonResponse
from user_activities.models import ActivityPeriods

def send_json(request):
	user_dict = {'ok':True,
				'members': []
			}
	activities = []
	for act in ActivityPeriods.objects.all():
		start_time = act.start_time.strftime("%b %d %Y %H:%M %p")
		end_time = act.end_time.strftime("%b %d %Y %H:%M %p")
		activities.append({
							'start_time': start_time,
							'end_time': end_time
						})
		user_dict['members'].append({
									'id': act.user.id,
									'real_name': act.user.real_name,
									'tz': act.user.time_zone,
									'activity_periods': activities
								})
	
	return JsonResponse(user_dict, safe=False)