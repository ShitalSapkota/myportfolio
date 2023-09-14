from django.urls import path

from . import views
# from website.views import about

urlpatterns = [
    path('', views.index, name='index'),

]