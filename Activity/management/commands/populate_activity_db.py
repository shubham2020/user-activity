from django.core.management.base import BaseCommand
from Member.models import User
from Activity.models import ActivityPeriod
import pytz
import random
import datetime

class Command(BaseCommand):

    def _create_tags(self):
        userList = User.objects.all()
        for user in userList:
            pivot_time = datetime.datetime.now() - datetime.timedelta(weeks=random.randint(24,48))
            for i in range(random.randint(1,5)):
                start_time = pivot_time + datetime.timedelta(days=i*20)
                end_time = start_time + datetime.timedelta(minutes=i*15)
                start_time = pytz.timezone(user.timeZone).localize(start_time)
                end_time = pytz.timezone(user.timeZone).localize(end_time)
                ActivityPeriod.objects.create(user=user, start_time=start_time, end_time=end_time)

    def handle(self, *args, **options):
        self._create_tags()