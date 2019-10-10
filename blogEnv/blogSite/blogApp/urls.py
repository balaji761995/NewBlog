from django.urls import path
from blogApp import views

urlpatterns = [
    path('about/',views.About.as_view(),name='about'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePost.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.UpdatePost.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',views.DeletePost.as_view(),name='post_remove'),
    path('draft/',views.DraftPost.as_view(),name='draft'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='post_comment'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish')
]
