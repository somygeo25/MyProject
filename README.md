<h4>Django Project</h4>
Framework- Django, Language- Python <br/>
This project create tables, write dummy data in database and fetch those data and dispalay in json format using API, <br/>
"trydjango" is the django files folder name<br/>
'user_activities' is the app name <br/>
Created two models named ActivityPeriods and Users<br/>
http://127.0.0.1:8000/sendjson/ is the API url to display the fetched data in json format
status of django project - actively working

# Commands used to populate data into database
from user_activities.models import Users, ActivityPeriods
activity_id = ActivityPeriods(start_time="2011-09-01T13:20:30+03:00", end_time="2011-09-03T13:20:30+03:00")
activity_id.save()
user_id = Users(real_name="Egon Spengler", time_zone="ASIA")
user_id.save()
user_id.activity.add(activity_id)
activity_id = ActivityPeriods(start_time="2011-09-11T13:20:30+03:00", end_time="2011-09-13T13:20:30+03:00")
activity_id.save()
user_id = Users(real_name="Glinda Southgood", time_zone="AMERICA")
user_id.save()
user_id.activity.add(activity_id)

