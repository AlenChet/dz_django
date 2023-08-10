from django.shortcuts import render
from .models import Article, Section


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().order_by('-published_at')
    sections = Section.objects.all()
    context = {
        'articles': articles,
        'sections': sections
    }
    return render(request, template, context)
