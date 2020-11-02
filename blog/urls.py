from django.urls import path
from . import views
# the import of . imports all of the views from out blog

# set the app name
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>', views.detail, name='detail'),
]    