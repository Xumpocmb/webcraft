from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleComment
from django.contrib.auth.models import User

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'app_blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'app_blog/article_detail.html', {'article': article})

def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.likes += 1
    article.save()
    return redirect(request.META.get('HTTP_REFERER', 'app_blog:article_list'))

def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # For simplicity, we'll assume the user is logged in to comment
        # In a real application, you would have a form here
        if request.user.is_authenticated:
            comment_text = request.POST.get('comment')
            if comment_text:
                ArticleComment.objects.create(
                    article=article,
                    author=request.user,
                    comment=comment_text
                )
    return redirect('app_blog:article_detail', pk=pk)