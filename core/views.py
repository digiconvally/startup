from django.shortcuts import render, get_object_or_404
from .models import Post


def Home(request):
    queryset = Post.objects.all()

    context = {
        'posts': queryset
    }
    return render(request, 'core/home.html', context)


def detaillistViews(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'objects': post
    }
    return render(request, 'core/detail.html', context)
