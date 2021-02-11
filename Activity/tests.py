from django.test import TestCase
from Activity.models import ActivityPeriod
from Member.models import User
import pytz
import random
import datetime

class ActivityTestCase(TestCase):

    '''
    To assertion test the correctness of the ActivityPeriod Model
    '''

    def setUp(self):
        activityList = []
        userList = []

        for name in ['shelly', 'sharon', 'sherman', 'shezwan', 'shakeel', 'sharmila']:
            tz = pytz.common_timezones[random.randint(0,len(pytz.common_timezones)-1)]
            userList.append(User.objects.create(username=name, timeZone=tz))

        for user in userList:
            pivot_time = datetime.datetime.now() - datetime.timedelta(weeks=random.randint(24,48))
            for i in range(random.randint(1,5)):
                start_time = pivot_time + datetime.timedelta(days=i*20)
                end_time = start_time + datetime.timedelta(minutes=i*15)
                start_time = pytz.timezone(user.timeZone).localize(start_time)
                end_time = pytz.timezone(user.timeZone).localize(end_time)
                obj = ActivityPeriod.objects.create(user=user, start_time=start_time, end_time=end_time)
                activityList.append(obj)
        
        return activityList

    def ActivityModelTest(self):
        objectList = self.setUp()
        for object in objectList:
            self.assertTrue(isinstance(object, ActivityPeriod), "ActivityPeriod Model Check Failed")
