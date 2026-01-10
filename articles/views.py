from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import HttpResponseForbidden

# Create your views here.

@login_required
def reporter_dashboard(request):
    if request.user.role != 'reporter':
        return HttpResponseForbidden("You do not have permission to access this page.")
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard/reporter_dashboard.html", {"articles": articles} )


@login_required
def article_create(request):
    if request.user.role != 'reporter':
        return HttpResponseForbidden("You do not have permission to create articles.")
    if request.method == "POST":
        title = request.POST.get("title")
        body = body,
        
        Article.objects.create(
            title=title, 
            slug=slugify(title), 
            body=body,
            author=request.user,
            status="draft",
        )
        return redirect("reporter_dashboard")
    return render(request, "articles/article_form.html")

@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.author:
        return HttpResponseForbidden("You do not have permission to edit this article.")
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.body = request.POST.get("body")
        article.slug = slugify(article.title)
        article.save()
        return redirect("reporter_dashboard")
    return render(request, "articles/article_form.html", {"article": article})


def home(request):
    articles = Article.objects.filter(status="published").order_by("-published_at")
    return render(request, "articles/home.html", {"articles": articles})