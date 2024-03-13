from django.urls import path

from . import views
from .admin import blog_site

urlpatterns = [
    path('myadmin/', blog_site.urls),
    path('', views.index, name='index'),
]
