from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TimeInView.as_view(), name='index'),
]
