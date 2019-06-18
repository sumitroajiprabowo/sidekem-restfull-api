import os
import json
from areacode.models import Regency
from django.core.management.base import BaseCommand
from config.settings import BASE_DIR


class Command(BaseCommand):
    """Import Regencies json to Database"""

    def import_regencies_from_json(self):
        data_folder = os.path.join(BASE_DIR, 'core', 'resources/regencies')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file),
                      encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    id = data_object.get('id', None)
                    name = data_object.get('name', None)
                    province_id = data_object.get('province_id', None)

                    try:
                        regencies, created = Regency.objects.get_or_create(
                            id=id,
                            name=name,
                            province_id=province_id
                        )
                        if created:
                            regencies.save()
                            display_format = \
                                "Data Regency, {}, has been saved."
                            print(display_format.format(regencies.name))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this Regencies: \
                            {}\n{}".format(name, str(ex))
                        print(msg)

    def handle(self, *args, **options):
        """Call the function to import data"""
        self.import_regencies_from_json()
