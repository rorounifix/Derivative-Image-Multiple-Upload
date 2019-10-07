from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings


from .models import ImageModel

class HomeView(generic.TemplateView):
    template_name = 'upload/index.html'


class AlbumView(generic.ListView):
    model = ImageModel
    # paginate_by = 6
    template_name = 'upload/album.html'
    context_object_name = 'imagelist'




def delete(request, id):
    d = ImageModel.objects.get(pk=id)
    name = d.image_name
    d.delete()
    os.remove(os.path.join(settings.MEDIA_ROOT, name))

    return HttpResponseRedirect(reverse('upload:album'))

@csrf_protect
def fileupload(request):
    fs = FileSystemStorage()
    for img in request.FILES.getlist('images'):
        print(img.file)
        name = fs.save(img.name, img)
        file_url = fs.url(name)
        m = ImageModel(image_name=name, image_url=file_url, image_date=timezone.now())
        m.save()
    return HttpResponseRedirect(reverse('upload:index'))



#
#
# class UploadView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.filter(
#         pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
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
