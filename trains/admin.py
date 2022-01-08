from django.contrib import admin

from trains.models import Train

class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    # добавляются поля в админке
    list_editable = ('travel_time',)  # эти поля можно редактировать 

admin.site.register(Train, TrainAdmin)   # регистрируем классы в админке
