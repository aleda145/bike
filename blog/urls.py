from django.conf.urls import url

from blog import views
from blog.views import ArticleMonthArchiveView
from django.views.generic.dates import MonthArchiveView
from blog.models import BlogPost
app_name= 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='blog_main'),

    #for some reason you _have_ to have the numeric first, otherwise it wont work
    # Example: /2012/08/
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        ArticleMonthArchiveView.as_view(month_format='%m'),
        name="archive_month_numeric"),
    #example 2012/mar
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',
        ArticleMonthArchiveView.as_view(),
        name="archive_month"),


    url(r'^reverse/$', views.ReversePostView.as_view(), name='reverse'),
        url(r'^archive/$', views.BlogArchiveView.as_view(), name='archive'),

    url(r'^(?P<slug>.+)/$', views.BlogPostDetail.as_view(), name='detail'),

    # Example: /2012/aug/

]

