"""
Import json data from JSON file to Datababse
"""
import os
import json
from task_app.models import Task
from django.core.management.base import BaseCommand
from datetime import datetime
from nasaq.settings import BASE_DIR


class Command(BaseCommand):
    def import_task_from_file(self):
        data_folder = os.path.join(BASE_DIR, 'task_app', 'resources/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    title = data_object.get('title', None)
                    description = data_object.get('description', None)
                    print(title)
                    # url = data_object.get('url', None)
                    # release_year = datetime.now()
                    #
                    try:
                        task, created = Task.objects.get_or_create(
                            title=title,
                            description=description,
                        )
                        if created:
                            task.save()
                            display_format = "\Task, {}, has been saved."
                            print(display_format.format(task))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this task: {}\n{}".format(title, str(ex))
                        print(msg)


    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_task_from_file()
