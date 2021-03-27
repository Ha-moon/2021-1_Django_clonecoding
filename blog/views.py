from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 쿼리셋을 담은 변수posts 생성.(쿼리셋의 이름붙여줌)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST": # 폼에 입력된 데이터를 view 페이지로 가지고 올 때(뭐 쓴 후 저장할때)
        form = PostForm(request.POST)
        if form.is_valid(): # 폼에 들어있는 값들이 올바른지 확인
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) # 새로 작성한 글 페이지로 넘어감
    else: # 처음 페이지에 접속했을 때
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})