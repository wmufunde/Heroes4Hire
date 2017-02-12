from django.conf.urls import url
from missions import views

urlpatterns = [
    url(r'^customer/$', views.CustomerView.as_view(), name='customer_signup'),
    url(r'^mission/$', views.MissionView.as_view(), name='mission_signup'),
    url(r'^report/$', views.ReportView.as_view(), name='report_signup'),
    url(r'^customer_list/$', views.customer_list, name='customer_list'),
    url(r'^customer/(?P<pk>[0-9]+)/$',views.CustomersUpdateView.as_view(), name='customer_update'),
    
    ]