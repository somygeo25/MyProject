<h2>Django Project</h2>
Framework- Django, Language- Python <br/>
This project create tables, write dummy data in database and fetch those data and dispalay in json format using API, <br/>
"trydjango" is the django files folder name<br/>
'user_activities' is the app name <br/>
Created two models named ActivityPeriods and Users<br/>
http://127.0.0.1:8000/sendjson/ is the API url to display the fetched data in json format<br/>
status of django project - actively working<br/>

<h4>Commands used to populate data into database</h4>
from user_activities.models import Users, ActivityPeriods<br/>
activity_id = ActivityPeriods(start_time="2011-09-01T13:20:30+03:00", end_time="2011-09-03T13:20:30+03:00")<br/>
activity_id.save()<br/>
user_id = Users(real_name="Egon Spengler", time_zone="ASIA")<br/>
user_id.save()<br/>
user_id.activity.add(activity_id)<br/>
activity_id = ActivityPeriods(start_time="2011-09-11T13:20:30+03:00", end_time="2011-09-13T13:20:30+03:00")<br/>
activity_id.save()<br/>
user_id = Users(real_name="Glinda Southgood", time_zone="AMERICA")<br/>
user_id.save()<br/>
user_id.activity.add(activity_id)<br/>

