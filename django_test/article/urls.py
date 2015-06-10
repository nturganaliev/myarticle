from django.conf.urls import url


urlpatterns = [
    url(r'^all/$', 'article.views.articles', name='articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article', name='article'),
    url(r'^create/$', 'article.views.create'),
    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
]