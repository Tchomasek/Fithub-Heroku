from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings

from .forms import PostForm
from .models import Post

def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    post_list = [{"id": x.id, "content": x.content, 'chat': x.chat, 'user': x.user.username} for x in qs]
    data = {
        "response": post_list
    }
    return JsonResponse(data)

def post_create_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    form = PostForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user or None
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = PostForm()
    return render(request, 'components/form.html', context={"form": form})