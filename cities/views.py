from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages import success


from . import forms
from cities.models import City

def home(request, pk=None):
    if request.method == 'POST':
        form = forms.CityForm(request.POST)
        if form.is_valid():  # проверяет валидность типа
            print(form.cleaned_data)
            form.save() # coхраняем в бд
    # if pk:
        # city = City.objects.filter(id=pk).first()  ||||| разные варианты
        # city = City.objects.get(id=pk)             ||||| обработки несуществующих id
        # city = get_object_or_404(City, id=pk)
        # context = {
        # 'object': city,
        # }
        # return render(request, 'cities/detail.html', context=context)
    form = forms.CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'form': form
    }
    return render(request, 'cities/home.html', context=context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"



class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = forms.CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home') # формируем отложенный вызов,  redirect
    success_message = "City was created successfully"


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = forms.CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "City was updated successfully"


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'   # c подтверждение удаления
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        success(request, 'City was deleted successfully')
        return self.post(request, *args, **kwargs)  # без подтверждения


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        form = forms.CityForm()
        # Add in a QuerySet of all the books
        context['form'] = form
        return context
