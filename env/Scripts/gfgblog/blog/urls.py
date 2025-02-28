# importing django routing libraries
from . import views
from django.urls import path, include
from .views import *
urlpatterns = [
	# home page
	path('', views.postslist.as_view(), name='posts'),
	# route for posts
	path('post/<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
]
