from rest_framework import serializers
from Activity.models import ActivityPeriod

FORMAT = "%b %d %Y %H:%M:%S%p"

class ActivityPeriodSerializer(serializers.ModelSerializer):

    '''
    To serialize the model data with minor modifications as per the date time display requirements
    '''

    start_time = serializers.DateTimeField(format=FORMAT)
    end_time = serializers.DateTimeField(format=FORMAT)

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']