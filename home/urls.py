from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from home import views as home_views


urlpatterns = [
    url('^$', home_views.home_page, name='home_page')
    
    ]