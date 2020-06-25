# from django.shortcuts import render

# # Create your views here.
# from datetime import datetime
# from django.db import models
# from django.http import JsonResponse
# from products.models import Users, ActivityPeriods

# def send_json(request):
# 	# user = Users.objects.create(real_name="anu", time_zone="ASIA")
# 	# user.save()
# 	# activity_id = ActivityPeriods.objects.create(start_time="2011-09-01T13:20:30+03:00", end_time="2011-09-01T13:20:30+03:00")
# 	# activity_id.save()
# 	# act_list = list(activity_id.id)
# 	# user.activity.add(activity_id)
# 	user_dict = {'ok':True,
# 				'members': []
# 			}
# 	# could not write values into manyToMany field that is why externally a list "activities" defined
# 	activities = []
	

# 	for act in ActivityPeriods.objects.all():
# 		start_time = act.start_time.strftime("%b %d %Y %H:%M:%S")
# 		end_time = act.end_time.strftime("%b %d %Y %H:%M:%S")
# 		activities.append({'start_time': start_time,
# 							'end_time': end_time})
# 	for user_id in Users.objects.all():
# 		# print(user_id.get_time_zone_display())
# 		reason = user_id.cleaned_data.get('time_zone')
# 		time = dict(user_id.fields['time_zone'].choices)[reason]
# 		print('timedddddddddddd')
# 		print(time)
# 		user_dict['members'].append({'id': user_id.id,
# 									'real_name': user_id.real_name,
# 									'tz': user_id.time_zone,
# 									'activity_periods': activities
# 								})
	
# 	return JsonResponse(user_dict, safe=False)