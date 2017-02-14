from django.conf.urls import url
from django.views.generic.base import TemplateView
from training import views

urlpatterns = [
    url(r'^attendance/$', views.AttendanceView.as_view(), name='attendance_signup'),
     url(r'^class/$', views.ClassView.as_view(), name='class_signup'),
    url(r'^trainer/$', views.TrainerView.as_view(), name='trainer_signup'),
    url(r'^room/$', views.RoomView.as_view(), name='room_signup'),
     url(r'^success/$', TemplateView.as_view(template_name='success.html'), name='success_page'),
    url(r'^class_profile/(?P<pk>\d+)/$', views.ClassProfileView.as_view(), name='class_profile'),
    url(r'^class_list/$', views.class_list, name='class_list'),
    url(r'^room_list/$', views.room_list, name='room_list'),
    url(r'^trainer_list/$', views.trainer_list, name='trainer_list'),
    url(r'^trainer_profile/(?P<pk>\d+)/$', views.TrainerProfileView.as_view(), name='trainer_profile'),
    url(r'^room/(?P<pk>[0-9]+)/$',views.RoomUpdateView.as_view(), name='room_update'),
    url(r'^room/(?P<pk>[0-9]+)/delete/$',views.RoomDeleteView.as_view(), name='room_delete'),
    url(r'^trainer/(?P<pk>[0-9]+)/$',views.TrainerUpdateView.as_view(), name='trainer_update'),
    url(r'^trainer/(?P<pk>[0-9]+)/delete/$',views.TrainerDeleteView.as_view(), name='trainer_delete'),
     url(r'^class/(?P<pk>[0-9]+)/$',views.ClassUpdateView.as_view(), name='class_update'),
    url(r'^class/(?P<pk>[0-9]+)/delete/$',views.ClassDeleteView.as_view(), name='class_delete'),
]