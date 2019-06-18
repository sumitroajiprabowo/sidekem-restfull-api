import os
import json
from areacode.models import District
from django.core.management.base import BaseCommand
from config.settings import BASE_DIR


class Command(BaseCommand):
    """Import Districts json to Database"""

    def import_districts_from_json(self):
        data_folder = os.path.join(BASE_DIR, 'core', 'resources/districts')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file),
                      encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    id = data_object.get('id', None)
                    name = data_object.get('name', None)
                    regency_id = data_object.get('regency_id', None)

                    try:
                        districts, created = District.objects.get_or_create(
                            id=id,
                            name=name,
                            regency_id=regency_id
                        )
                        if created:
                            districts.save()
                            display_format = \
                                "Data District, {}, has been saved."
                            print(display_format.format(districts.name))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this District: \
                            {}\n{}".format(name, str(ex))
                        print(msg)

    def handle(self, *args, **options):
        """Call the function to import data"""
        self.import_districts_from_json()
