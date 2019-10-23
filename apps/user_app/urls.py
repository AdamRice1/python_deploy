from django.conf.urls import url
from . import views

                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^sign_in$', views.sign_in),
    url(r'^create$', views.create),
    url(r'^user$', views.user),
    url(r'^create_user$', views.create_user),
    url(r'^login$', views.login),
    url(r'^create_biz$', views.create_biz),
    url(r'^business_dashboard/(?P<x>\d+)$', views.biz_dashboard),
    url(r'^delete/(?P<y>\d+)$', views.delete),
    url(r'^logout$', views.logout),
    url(r'^data/(?P<y>\d+)$', views.data_page),
    url(r'^input_data/(?P<y>\d+)$', views.input_data),
    url(r'^input_retire_data/(?P<y>\d+)$', views.retirement_data),
    url(r'^input_retirement_data$', views.input_retire_data),
    url(r'^change_retire_data/(?P<y>\d+)$', views.change_retire_data),
    url(r'^change_retirement_data$', views.change_retirement_plan),
    url(r'^input_first_time$', views.first_time_data),
]