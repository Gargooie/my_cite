from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse


from .models import Post, Comment
from .forms import CommentForm

# old posts DB
# all_posts = [
#     {}
# ]


def get_date(post):
    return post['date']


def index(request):
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    DB_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        # 'posts': latest_posts
        'posts': DB_posts
    })
class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:3]
        return data


def posts(request):
    DB_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": DB_posts
    })

class postsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


# def post_detail(request, slug):
#     # identified_post = next(post for post in all_posts if post['slug'] == slug)
#     the_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": the_post,
#         "post_tags": the_post.tags.all(),
#
#     })

class PostDetailView(View):
    # template_name = "blog/post-detail.html"
    # model = Post
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later


    def get(self, request,slug):
        post=Post.objects.get(slug=slug)

        context =  {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self,request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post_detail_page", args=[slug]) )

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all(),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context

# my own send comment method
# def comment_send(request):
#     print("check work")
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         comment_send = Comment(
#             name=request.POST["name"],
#             email="test@gmail.com",
#             comment_text=request.POST["comment_text"])
#         comment_send.save()
#
#         post_comment= Post.objects.all()[0].title="going2"
#         post_comment.save()
#         # return HttpResponseRedirect(reverse("post_detail_page", args=[slug]) )

    #
    # return render(request, "blog/includes/comment.html")


class AddFavoriteView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {

        }

        if stored_posts is None or len(stored_posts) ==0:
            context["posts"] = []
            context["has_posts"]= False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"]= True

        return render(request, "blog/favorites.html", context)

    def post(self, request):

        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(int(post_id))
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")

    # my old own stored posts function
        # post_id = request.POST["post_id"]
        #
        # post_slug=request.POST["post_slug"]
        # for x in request.session["favorite_post"]:
        #     print(type(x))
        #     print(x)
        #
        # print("favorite is " + post_id + " "+ post_slug)
        #
        # if post_id not in request.session["favorite_post"]:
        #     request.session["favorite_post"] += post_id
        #     print("added " + post_id)
        # else:
        #     request.session["favorite_post"].remove(post_id)
        #     print("removed " + post_id)
        #
        #
        #
        # for item in request.session["favorite_post"]:
        #     print(item)
        #
        #
        # return HttpResponseRedirect("/posts/" + post_slug)


#
# class WatchFavoriteView(View):
#     def post(self, request):
#         post_ids = request.session["favorite_post"]
#         return render(request, "blog/favorites.html", {
#             "posts": post_ids
#         })
#
#
#     def get(self, request):
#         post_ids = request.session["favorite_post"]
#         DB_posts = Post.objects.filter(id__in=post_ids)
#         return render(request, "blog/favorites.html", {
#             "posts": DB_posts
#         })
#
#     def favorite_posts(request):
#         DB_posts = Post.objects.all().order_by("-date")
#
#         post_id=request.session["post_id"]
#
#         return render(request, "blog/all-posts.html", {
#             "all_posts": DB_posts
#         })