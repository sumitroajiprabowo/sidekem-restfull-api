from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Import Groups to Database"""

    def import_groups(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        group, created = Group.objects.get_or_create(name="province")
        if created:
            group.name = "province"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

        group, created = Group.objects.get_or_create(name="regency")
        if created:
            group.name = "regency"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

        group, created = Group.objects.get_or_create(name="district")
        if created:
            group.name = "district"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

        group, created = Group.objects.get_or_create(name="village")
        if created:
            group.name = "village"
            group.save()
            display_format = \
                "Groups {} has been saved."
            print(display_format.format(group.name))
        else:
            display_format = \
                "Groups {} already available."
            print(display_format.format(group.name))

    def handle(self, *args, **options):
        """Call the function to import Groups"""
        self.import_groups()
