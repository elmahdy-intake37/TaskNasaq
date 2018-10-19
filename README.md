# TaskNasaq
to insert dummy data using:
python manage.py loade_random_task_data.py

u can modify your data in file json in folder resources

url:
localhost:8000/get_state/
params need to send:
name of state as name of class
id,
title
disc
for example


{
	"state": "New()",
	"id":"1",
	"title":"task01",
	"des":"desc6",
	"ref_id": "10"
}
