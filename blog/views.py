from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 쿼리셋을 담은 변수posts 생성.(쿼리셋의 이름붙여줌)
    return render(request, 'blog/post_list.html', {'posts':posts})
