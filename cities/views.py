from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


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
    context = {
        'object_list': qs,
        'form': form
    }
    return render(request, 'cities/home.html', context=context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"



class CityCreateView(CreateView):
    model = City
    form_class = forms.CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home') # формируем отложенный вызов,  redirect


class CityUpdateView(UpdateView):
    model = City
    form_class = forms.CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')



class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'   # c подтверждение удаления
    success_url = reverse_lazy('cities:home')

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)  # без подтверждения
