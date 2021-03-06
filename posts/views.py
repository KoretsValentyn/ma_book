from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import PostForm, EditPostForm
from .models import Post


def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], text=form.cleaned_data['text'], author=request.user)
            post.save()
            return redirect(reverse('posts:show'))
    return render(request, 'create.html', {'form': form})


def edit(request):
    post = get_object_or_404(Post, slug_title=request.GET['slug_title'])
    form = EditPostForm(instance=post)
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        form.save()
        return redirect(reverse('posts:show'))
    return render(request, 'edit.html', {'form': form})


def show(request):
    post = Post.objects.filter(author=request.user.id)
    return render(request, 'posts_list.html', {'posts': post})
