from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'apps/index.html'
    context_object_name ='latest_question_list'

    def get_queryset(self):
        """Return last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = "app_name"
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = 'apps/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['title'] = "app_name"
        return context


class ResultView(generic.DetailView):
    model = Question
    template_name = 'apps/results.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['title'] = "app_name"
        return context


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'apps/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
            'title': 'app_name',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app_name:results', args=(p.id,)))


