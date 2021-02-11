from django.contrib import admin
from Activity.models import ActivityPeriod

class ActivityPeriodAdmin(admin.ModelAdmin):
    '''
    Selecting fields to display in the admin page
    '''

    list_display = ("start_time", "end_time", "user")

admin.site.register(ActivityPeriod, ActivityPeriodAdmin)