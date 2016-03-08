from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import BlogPost

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """
        Return the last five published Posts (not including those set to be
        published in the future).
        """
        return BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return BlogPost.objects.filter(pub_date__lte=timezone.now())

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
#         return render(request, 'blog/detail.html', {
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