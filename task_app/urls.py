from django.urls import path
from django.conf.urls import url, include

from task_app import views

urlpatterns = [
        # url(r'^get_state/(?P<string>.+)/$', views.get_state, name='get_state')
        url(r'^get_state/$', views.get_state, name='get state')

               ]
