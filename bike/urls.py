"""bike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^blog/', include ('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='blog_main'),
    url(r'^about/',views.AboutView.as_view(), name='about'),
    url(r'^equipment/',views.EquipmentView.as_view(), name='equipment'),
    url(r'^route/',views.RouteView.as_view(), name='route'),
    url('^reverse/',views.ReversePostView.as_view(),name='reverse'),
    url('^contact/',views.ContactView.as_view(),name='contact'),
    url('^thanks/',views.ThanksView.as_view(),name='contact'),
    url('^aboutsite/',views.AboutSiteView.as_view(),name='contact'),

]

