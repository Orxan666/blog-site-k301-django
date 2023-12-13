from django.shortcuts import render
from .models import Article, Author, Tag
# Create your views here.


def blog(request):
    author_username = request.GET.get("author")
    authors = Author.objects.all()  # SELECT * FROM blog_author;
    articles = Article.objects.all()  # SELECT * FROM blog_article;
    tags = Tag.objects.all()
    tag_title = request.GET.get("tag")
    if author_username:
        articles=articles.filter(author__user__username=author_username)
    if tag_title:
        articles=articles.filter(tags__title=tag_title)
    return render(request, 'blog.html', context={'articles': articles, 'authors': authors, 'tags': tags})


def blog_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, "blog-detail.html", context={'article': article})


def example(request):
    # name="Tunar"
    users = [
        {'name': 'orxan', 'age': 27, 'job': 'Sofware Developer'},
        {'name': 'eli', 'age': 24, 'job': 'Sofware Developer'},
        {'name': 'aysel', 'age': 21, 'job': 'Sofware Developer'},
        {'name': 'senan', 'age': 23, 'job': 'Sofware Developer'},
    ]
    return render(request, 'example.html', context={'users': users})
