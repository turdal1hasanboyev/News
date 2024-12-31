from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Article
from apps.common.models import Sub_Email
from apps.category.models import Category, Tag


def home_view(request):
    query = request.POST.get('query')
    sub_email = request.POST.get('sub_email')

    article = Article.objects.all()
    sport = article.filter(category__name="Sport")
    business = article.filter(category__name="Business")
    technology = article.filter(category__name="Technology")
    intertaiment = article.filter(category__name="Intertainment")

    if query:
        article = article.filter(title__icontains=query)
    if request.method == "POST" and sub_email:
        Sub_Email.objects.create(sub_email=sub_email)
        messages.success(request, "You have been subscribed successfully!")
        return redirect('/')

    context = {
        "banner": article.order_by("-id")[:2],
        "for_banner": article.order_by("id")[:4],
        "sport": sport.order_by("?")[:4],
        "business": business.order_by("id")[:4],
        "technology": technology.order_by("-id")[:4],
        "intertaiment": intertaiment.order_by("?")[:4],
        "articles": article.order_by("-created_at")[:9],
        "read_more": article.order_by("created_at")[:15],
        "featured_news": article.order_by('id')[:3],
        "popular_news": article.order_by('views')[:3],
        "latest_news": article.order_by('id')[:3],
        "most_view": article.order_by('views')[:3],
        "most_read": article.order_by('views')[:3],
        "most_recent": article.order_by('-views')[:3],
    }

    return render(request, 'index.html', context)

def article_detail_view(request, slug):
    sub_email = request.POST.get('sub_email')
    search = request.POST.get('query')

    template_name = 'single-page.html'

    article = Article.objects.get(slug__exact=slug)
    article.views += 1
    article.save()

    this_category_article = Article.objects.filter(category=article.category)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if search:
        this_category_article = this_category_article.filter(title__icontains=search)

    if request.method == "POST":
        if sub_email:
            Sub_Email.objects.create(sub_email=sub_email)
            messages.success(request, "You have successfully subscribed!")
            return redirect('article-detail', slug=article.slug)
        else:
            messages.error(request, "Please enter your email address!")
            return redirect('article-detail', slug=article.slug)

    context = {
        "article": article,
        "this_category_article": this_category_article.order_by("id")[:6].exclude(id=article.id),
        "related_articles": this_category_article.exclude(id=article.id).order_by("?")[:3],
        "categories": categories,
        "tags": tags,
        "featured_articles": this_category_article.exclude(id=article.id).order_by("id")[:3],
        "popular_articles": this_category_article.exclude(id=article.id).order_by("views")[:3],
        "recent_articles": this_category_article.exclude(id=article.id).order_by("id")[:3],
    }
    
    return render(request=request, template_name=template_name, context=context)
