from django.urls import path, re_path

from django.views.static import serve
from django.conf import settings

from . import views

urlpatterns=[
    path("", views.IndexView.as_view(), name="starting-page"),
    # path("comment", views.comment_send),
    path("best", views.AddFavoriteView.as_view(), name="favorites"),
    path("posts", views.postsView.as_view(), name="posts-page"),
     # path("posts/favorite", views.AddFavoriteView.as_view()),
    path("posts/<slug:slug>",views.PostDetailView.as_view(), name="post_detail_page"),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]
