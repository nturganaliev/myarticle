from django.shortcuts import render_to_response
from article.models import Article
from article.forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


def articles(request):
    return render_to_response('article/articles.html', {'articles': Article.objects.all()})


def article(request, article_id):
    return render_to_response('article/article.html', {'article': Article.objects.get(id=article_id)})


def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('create_article.html', args)


def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        a.likes += 1
        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)