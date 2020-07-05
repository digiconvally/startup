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


# def PostCreate(request):
# 	if request.method =='POST':
# 		form = PostForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			message.success(request, 'your message')
# 			return redirect('url')
# 	else:
# 	form : PostForm()
# 	context = {'form': form}
# 	return render(request, 'html', context)


# def PostUpdate(request, id):
#     post = get_object_or_404(Post, id=id)
#     form = PostForm(request.POST or None, instence=post)
#         if form.is_valid():
#            form.save()
#            return redirect('/article/list/')
#     return render(request, 'core/post_detail.html', {'form':form})


# def PostDelete(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method =='POST':
#         post.delete()
#         return redirect('/post/list/')
#     return render(request, 'core/post_detail.html', {'post':post})
