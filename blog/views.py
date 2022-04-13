from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (ListView, DetailView, TemplateView,
                                  CreateView, UpdateView, DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from blog.forms import PostForm, CommentForm
from blog.models import Comment, Post

import pusher

login_url = 'login'
post_detail = 'blog:post_detail'

class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView, LoginRequiredMixin):
    login_url = login_url
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = login_url
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostDraftList(ListView, LoginRequiredMixin):
    login_url = login_url
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


# --------------------------------------#
#     Functions that require a pk match #
# --------------------------------------#
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()

    # convert data list objects to json
    data = {
        'pk':post.pk,
        'title':post.title,
        'published_date':post.published_date.strftime("%a %b %Y"),
    }
    # send data to pusher
    pusher_client = pusher.Pusher(
        app_id='1383818',
        key='92577d85ff1ddd64974e',
        secret='452d2676c5c028b92d50',
        cluster='ap2',
        ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event', data)
    return redirect(post_detail, pk=pk)

# todo:uncomment it
# @login_required


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post_detail, pk=pk)

    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect(post_detail, pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect(post_detail, pk=post_pk)
