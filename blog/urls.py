from django.urls import path
from . import views


urlpatterns = [
    path('', views.StartingPageView.as_view(), name='home'),
    path('posts', views.AllPostsViews.as_view(), name='posts'),
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='single-post'), # slug will do this /// posts/my-first-post
    path('read-later', views.ReadLaterView.as_view(), name='read-later'),
 ]
