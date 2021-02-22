from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import PostForm
from .models import Post

def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    post_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": post_list
    }
    return JsonResponse(data)

def post_create_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = PostForm()
    return render(request, 'components/form.html', context={"form": form})