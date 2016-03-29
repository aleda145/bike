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

#TODO archive
class IndexView(ListView):
    context_object_name = 'posts_list'
    template_name = 'blog/blog_main.html'
    paginate_by = 5


    ####queryset is returned to the template, but first it is cut in pages of 5 by pagination.
    queryset = BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    print(queryset)
# class IndexView(generic.ListView):
#     template_name = 'blog/blog_base.html'
#     context_object_name = 'posts_list'
#     paginate_by = 5
#     def get_queryset(self):
#         """
#         Return the last five published Posts (not including those set to be
#         published in the future).
#         """
#         print(BlogPost.objects.filter(pub_date__lte=timezone.now()))
#
#         context=BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
#         return context


#returns the blog posts in the opposite order, so starting with the first post added to the database
class ReversePostView(IndexView):
    template_name= 'blog/blog_reverse.html'

    paginate_by = 5
    def get_queryset(self):


        return BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')



class ArticleMonthArchiveView(MonthArchiveView, IndexView):
    template_name = 'blog/blog_base.html'
    queryset = BlogPost.objects.all()
    date_field = "pub_date"
    allow_future = True
    paginate_by = 0

class BlogArchiveView(IndexView):
    template_name = 'blog/blog_archive.html'
    paginate_by = 0

class BlogPostDetailView(DetailView):
    template_name = 'blog/blog_detail.html'

    context_object_name = 'posts_list'

    queryset = BlogPost.objects.filter(pub_date__lte=timezone.now())
    #model = BlogPost
    #paginate_by=0
   # print('wow')
   # print(queryset)

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class EquipmentView(ListView):
    template_name = 'blog/equipment.html'
    context_object_name = 'equipment_list'
    # print('eq cat')
    # print(EquipmentCategory.objects.all())
    # print('eq items')
    # print(EquipmentItem.objects.all())
    # print(EquipmentCategory.objects.get(id=1).equipmentitem_set.all())
    #print(EquipmentCategory.equipmentitem_set.all())
    #for equipmentitem in EquipmentCategory.equipmentitem_set.all():
        #print(equipmentitem)
   # print('for lop')
    data={}
    for item in EquipmentCategory.objects.all():
        data[item]=item.equipmentitem_set.all()
       # print('item')
       # print(item)
        #print('items')
        #print(item.equipmentitem_set.all())

   # print('data')
    print(data)
    queryset = data
class RouteView(TemplateView):
    template_name = 'blog/route.html'

class ContactView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
    def form_valid(self, form):
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            name=form.cleaned_data['name']
            print(name)
            try:
                send_mail(subject+' '+name, message, from_email, ['alexander.dahl93@gmail.com'])
                print('email sent!')
            except BadHeaderError:
                    return HttpResponse('Invalid header found.')

        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ContactView, self).form_valid(form)

class ThanksView(TemplateView):
    template_name = 'blog/thanks.html'
# class DetailView(generic.DetailView):
#     template_name = 'blog/blog_detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return BlogPost.objects.filter(pub_date__lte=timezone.now())

        # class ResultsView(generic.DetailView):
        #     model = Question
        #     template_name = 'blog/results.html'

        #
        # def vote(request, question_id):
        #     question = get_object_or_404(Question, pk=question_id)
        #     try:
        #         selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #     except (KeyError, Choice.DoesNotExist):
        #         # Redisplay the question voting form.
        #         return render(request, 'blog/blog_detail.html', {
        #             'question': question,
        #             'error_message': "You didn't select a choice.",
        #         })
        #     else:
        #         selected_choice.votes += 1
        #         selected_choice.save()
        #         # Always return an HttpResponseRedirect after successfully dealing
        #         # with POST data. This prevents data from being posted twice if a
        #         # user hits the Back button.
        #         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))