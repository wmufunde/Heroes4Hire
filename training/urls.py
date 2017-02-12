from django.conf.urls import url
from django.views.generic.base import TemplateView
from training import views

urlpatterns = [
    url(r'^attendance/$', views.AttendanceView.as_view(), name='attendance_signup'),
     url(r'^class/$', views.ClassView.as_view(), name='class_signup'),
    url(r'^trainer/$', views.TrainerView.as_view(), name='trainer_signup'),
    url(r'^room/$', views.RoomView.as_view(), name='room_signup'),
     url(r'^success/$', TemplateView.as_view(template_name='success.html'), name='success_page'),
]