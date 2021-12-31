from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from cities.models import City

def home(request, pk=None):
    # if pk:
        # city = City.objects.filter(id=pk).first()  ||||| разные варианты
        # city = City.objects.get(id=pk)             ||||| обработки несуществующих id
        # city = get_object_or_404(City, id=pk)
        # context = {
        # 'object': city,
        # }
        # return render(request, 'cities/detail.html', context=context)
    qs = City.objects.all()
    context = {
        'object_list': qs,
    }
    return render(request, 'cities/home.html', context=context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"