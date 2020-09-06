from django.urls import path
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='blog'
    ),
    path(
        route='posts/<slug:url>/',
        view=views.view_post, 
        name='detail'
    ),
    path(
        route='posts/save_comment',
        view=views.save_comment,
        name='save_comment'
    ),

   
    #path('com/<slug:url>', views.sendComment,name='sendComment'),

    path('posts/search', views.SearchResultsView.as_view(), name='search_results'),


    path('post_edit/<slug:url>/', views.PostsUpdate, name='post_edit'),
]
