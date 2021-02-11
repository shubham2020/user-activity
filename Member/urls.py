from django.urls import path, include

urlpatterns = [
    path('apis/', include('Member.apis.urls')),
]
