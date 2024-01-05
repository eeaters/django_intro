from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def hello_world(request):
    return HttpResponse("Hello World!")


def article_content(request):
    article = Article.objects.all()[0]
    return HttpResponse(
        f'id: {article.id} , title: {article.title}, content: {article.content}, date: {article.publish_date}')


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    articles = Article.objects.all()
    paginator = Paginator(articles,3)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)

    if page_article_list.has_next():
        next_page = page +1
    else:
        next_page = page

    if page_article_list.has_previous():
        previous_page = page -1
    else:
        previous_page = page


    top5_articles = Article.objects.order_by('-publish_date')[:5]

    return render(request,
                  'blog/index.html',
                  {
                      'article_list': page_article_list,
                      'page_num': range(1,page_num+1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': previous_page,
                      'top5_articles': top5_articles
                  })


def get_detail_page(request, article_id):
    articles = Article.objects.all()

    current_index = -1
    for i in range(articles.count()):
        if (article_id == articles[i].id):
            current_index = i

    pre_article = None
    post_article = None
    if current_index > 0:
        pre_article = articles[current_index - 1]
    if current_index >= 0 and current_index < articles.count() - 1:
        post_article = articles[current_index + 1]

    return render(request,
                  'blog/detail.html',
                  {
                      'curr_article': articles[current_index],
                      'pre_article': pre_article,
                      'post_article': post_article
                  })
