from django.urls import path
import Member.apis.views as views

urlpatterns = [
    path('member-activity/', views.memberActivityList, name='memberActivityList'),
]
