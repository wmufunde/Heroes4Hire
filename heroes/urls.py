from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from heroes import views

urlpatterns = [
    url(r'^heroessignup/$', login_required(views.HeroesView.as_view()), name='heroes_signup'),
     url(r'^team/$', views.TeamView.as_view(), name='team_signup'),
    url(r'^status/$', views.StatusView.as_view(), name='status_log'),
    url(r'^currentteam/$', views.CurrentteamView.as_view(), name='team_log'),
     url(r'^successcurrentteam/$', TemplateView.as_view(template_name='successcurrentteam.html'), name='success_current_team'),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile_page'),
    url(r'^profileimgupdate/(?P<pk>\d+)/$', views.PicupdateView.as_view(), name='pic_update'),
    url(r'^hero_list/$', views.hero_list, name='hero_list'),
    # URL for hero stats update
    url(r'^hero/(?P<pk>[0-9]+)/$',views.HeroesUpdateView.as_view(), name='hero_update'),
    url(r'^hero/(?P<pk>[0-9]+)/delete/$',views.HeroesDeleteView.as_view(), name='hero_delete'),
    url(r'^team_list/$', views.team_list, name='team_list'),
    url(r'^team_profile/(?P<pk>\d+)/$', views.TeamProfileView.as_view(), name='team_profile'),
    url(r'^hero/(?P<pk>[0-9]+)/$',views.HeroesUpdateView.as_view(), name='hero_update'),
    url(r'^team/(?P<pk>[0-9]+)/$',views.TeamUpdateView.as_view(), name='team_update'),
    url(r'^team/(?P<pk>[0-9]+)/delete/$',views.TeamDeleteView.as_view(), name='team_delete'),

]
