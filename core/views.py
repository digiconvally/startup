from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def Home(request):
    queryset = Post.objects.all().order_by('-created_at')

    context = {
        'posts': queryset
    }
    return render(request, 'core/home.html', context)


def PostCreate(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form: PostForm()
    context = {'form': form}
    return render(request, 'core/create.html', context)


def detaillistViews(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'objects': post
    }
    return render(request, 'core/detail.html', context)


def PostUpdate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'core/create.html', context)


def PostDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'core/delete.html', {'post': post})
