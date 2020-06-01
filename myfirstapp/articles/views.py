from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@login_required(login_url = '/accounts/login')
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article_detail.html', {'article':article})

def article_create(request):
    if forms.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form':form})
