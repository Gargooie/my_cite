from django.urls import path


from . import views

urlpatterns=[
    path("", views.IndexView.as_view(), name="starting-page"),
    # path("comment", views.comment_send),
    path("best", views.AddFavoriteView.as_view(), name="favorites"),
    path("posts", views.postsView.as_view(), name="posts-page"),
     # path("posts/favorite", views.AddFavoriteView.as_view()),
    path("posts/<slug:slug>",views.PostDetailView.as_view(), name="post_detail_page")



]
