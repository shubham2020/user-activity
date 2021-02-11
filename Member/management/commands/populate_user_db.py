from django.core.management.base import BaseCommand
from Member.models import User
import pytz
import random

class Command(BaseCommand):

    def _create_tags(self):
        for name in ['shelly', 'sharon', 'sherman', 'shezwan', 'shakeel', 'sharmila']:
            tz = pytz.common_timezones[random.randint(0,len(pytz.common_timezones)-1)]
            User.objects.create(username=name, timeZone=tz)

    def handle(self, *args, **options):
        self._create_tags()