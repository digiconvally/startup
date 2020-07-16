from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def Home(request):
    queryset = Post.objects.filter(feature=True).order_by('-created_at')
    context = {
        'posts': queryset
    }
    return render(request, 'core/home.html', context)


def PostCreate(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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
    obj = get_object_or_404(Post, pk=pk)

    form = PostForm(request.POST or None, instance=obj)

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


class PostListViews(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'core/home.html'
    ordering = '-created_at'


class PostDetailViews(DetailView):
    model = Post
    template_name = 'core/detail.html'


class PostUpdateViews(UpdateView):
    model = Post
    form_class = PostForm
    # success_url = '/'
    template_name = 'core/create.html'

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


class PostCreateViews(CreateView):
    form_class = PostForm
    template_name = 'core/create.html'
    # success_url = '/'

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


class PostDeleteViews(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'core/delete.html'
