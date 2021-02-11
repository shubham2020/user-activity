from django.urls import path, include

app_name = 'Member'

urlpatterns = [
    path('apis/', include('Member.apis.urls')),
]
