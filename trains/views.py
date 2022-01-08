from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages import success


from . import forms
from trains.models import Train

def home(request, pk=None):

    form = forms.TrainForm()
    qs = Train.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'trains/home.html', context=context)


class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'



class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = "trains/detail.html"



class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = forms.TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home') # формируем отложенный вызов,  redirect
    success_message = "Train was created successfully"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = forms.TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Train was updated successfully"


class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/delete.html'   # c подтверждение удаления
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        success(request, 'Train was deleted successfully')
        return self.post(request, *args, **kwargs)  # без подтверждения




