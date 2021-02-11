from django.test import TestCase
from Member.models import User
import pytz, random

class UserTestCase(TestCase):

    '''
    To assertion test the correctness of the User Model
    '''

    def setUp(self):
        objectList = []
        for name in ['shelly', 'sharon', 'sherman', 'shezwan', 'shakeel', 'sharmila']:
            tz = pytz.common_timezones[random.randint(0,len(pytz.common_timezones)-1)]
            objectList.append(User.objects.create(username=name, timeZone=tz))
        return objectList

    def UserModelTest(self):
        objectList = self.setUp()
        for object in objectList:
            self.assertTrue(isinstance(object, User), "User Model Check Failed")
