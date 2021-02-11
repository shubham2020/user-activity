from rest_framework import serializers
from Member.models import User
from Activity.serializers import ActivityPeriodSerializer


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='real_world_id')
    real_name = serializers.CharField(source='username')
    tz = serializers.CharField(source='timeZone')
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']

class StreamSerializer(serializers.Serializer):
    members = UserSerializer(many=True, read_only=True)
    ok = serializers.BooleanField(initial=True)