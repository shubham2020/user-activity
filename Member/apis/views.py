
from django.http import HttpResponse, JsonResponse
from Member.models import User
from Member.serializers import UserSerializer, StreamSerializer
from collections import namedtuple

def memberActivityList(request):
    """
    List all activities of all the users.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        Stream = namedtuple('Stream', ('ok', 'members'))
        stream = Stream(
            ok=True,
            members=users,
        )

        serializer = StreamSerializer(stream)

        return JsonResponse(serializer.data, safe=False)

    return HttpResponse(status=400)

    