from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.run_bot, name='run_bot'),
]