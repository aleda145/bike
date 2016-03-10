from django.conf.urls import url

from blog import views
from blog.views import ArticleMonthArchiveView
from django.views.generic.dates import MonthArchiveView
from blog.models import BlogPost
app_name= 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',
        ArticleMonthArchiveView.as_view(),
        name="archive_month"),
    # Example: /2012/08/
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        ArticleMonthArchiveView.as_view(month_format='%m'),
        name="archive_month_numeric"),


    # url(r'^articles/monthly/$',MonthArchiveView.as_view(
    #     model=BlogPost,
    #     paginate_by=12,
    #     date_field='pub_date',
    #     template_name='blog/monthly.html',
    # ),name="monthly"),
    url(r'^(?P<slug>.+)/$', views.DetailView.as_view(), name='detail'),

    # Example: /2012/aug/

]

