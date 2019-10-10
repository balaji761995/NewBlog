from django.shortcuts import render, get_object_or_404, redirect
from blogApp.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blogApp.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class About(TemplateView):
    template_name = 'blogApp/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_time__lte=timezone.now()).order_by('-published_time')

class PostDetailView(DetailView):
    model = Post

class CreatePost(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePost(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftPost(ListView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_time__isnull=True).order_by('published_time')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blogApp/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
