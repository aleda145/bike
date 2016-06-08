from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import TemplateView
from blog.forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.dates import MonthArchiveView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogPost,EquipmentItem,EquipmentCategory
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core.mail import send_mail, BadHeaderError

class IndexView(ListView):
    context_object_name = 'posts_list'
    template_name = 'blog/blog_main.html'
    paginate_by = 5
    queryset = BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class ReversePostView(IndexView):
    template_name= 'blog/blog_reverse.html'
    paginate_by = 5
    queryset = BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')

class ArticleMonthArchiveView(MonthArchiveView, IndexView):
    template_name = 'blog/blog_base.html'
    queryset = BlogPost.objects.all()
    date_field = "pub_date"
    allow_future = False
    paginate_by = 0

class BlogArchiveView(IndexView):
    template_name = 'blog/blog_archive.html'
    paginate_by = 0

class BlogPostDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'posts_list'
    queryset = BlogPost.objects.filter(pub_date__lte=timezone.now())

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class EquipmentView(ListView):
    template_name = 'blog/equipment.html'
    context_object_name = 'equipment_list'
    queryset=EquipmentCategory.objects.all()

class RouteView(TemplateView):
    template_name = 'blog/route.html'

class AboutSiteView(TemplateView):
    template_name = 'blog/aboutsite.html'

class ContactView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm

    success_url = '/thanks/'
    def form_valid(self, form):
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name=form.cleaned_data['name']
            print(name)
            try:
                send_mail(subject,name+'\nfrom:  '+from_email+'\n'+message, from_email, ['alexander.dahl93@gmail.com'])
                print('email sent!')

                send_mail('Thanks for your email!', 'Hi '+name+'! \nThank you for your email, I will try to get back to as soon as possible! \n\nBest regards\nAlex', 'Alex <alexander.dahl93@gmail.com>', [from_email])
            except BadHeaderError:
                    return HttpResponse('Invalid header found.')

        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ContactView, self).form_valid(form)

class ThanksView(TemplateView):
    template_name = 'blog/thanks.html'