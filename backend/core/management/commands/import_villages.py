import os
import json
from areacode.models import Village
from django.core.management.base import BaseCommand
from config.settings import BASE_DIR


class Command(BaseCommand):
    """Import Villages json to Database"""

    def import_villages_from_json(self):
        data_folder = os.path.join(BASE_DIR, 'core', 'resources/villages')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file),
                      encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    id = data_object.get('id', None)
                    name = data_object.get('name', None)
                    district_id = data_object.get('district_id', None)

                    try:
                        villages, created = Village.objects.get_or_create(
                            id=id,
                            name=name,
                            district_id=district_id
                        )
                        if created:
                            villages.save()
                            display_format = \
                                "Data Village, {}, has been saved."
                            print(display_format.format(villages.name))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this Villages: \
                            {}\n{}".format(name, str(ex))
                        print(msg)

    def handle(self, *args, **options):
        """Call the function to import data"""
        self.import_villages_from_json()
