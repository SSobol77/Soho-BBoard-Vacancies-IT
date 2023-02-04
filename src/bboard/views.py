from django.views.generic.edit import CreateView
from .models import Bb, Rubric
from django.shortcuts import render
from .forms import BbForm
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}

    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}

    return render(request, 'bboard/by_rubric.html', context)




''' Контроллер-class BbCreateView, который сам выполнит большую часть действий по выводу и обработке формы
    Контроллер-class мы сделали производным от класса CreateView из модуля django.views.generic.edit, базовый класс 
    знает как создать форму, вывести на экран страницу с применением УКАЗАННОГО шаблона:'''
class BbCreateView(CreateView):

    template_name = 'bboard/create.html'  # путь к шаблону файла, создающего страницу с формой
    form_class = BbForm   # ссылка на класс формы, связанной с моделью
    success_url = '/bboard/'  # интернет-адрес для перенаправления после успешного сохранения данных

    '''
    
    template_name = 'bboard/create.html'  # путь к шаблону файла, создающего страницу с формой
    from_class = BbForm  # ссылка на класс формы, связанной с моделью
    success_url = reverse_lazy('index')  # интернет-адрес для перенаправления после успешного сохранения данных(в нашем случае главная страница)
    # функция reverse_lazy() из модуля django.urls принимает имя маршрута и значения всех входящих в маршрут URL-параметров (если они там есть),
    # результатом будет готовый интернет адрес.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

 Переопределяем метод get_context_data, формирующий контекст шаблона, т.к. на каждой странице
сайта должен выводиться перечень рубрик. В теле метода  получаем контекст шаблона от метода базового класса,
добавляем в него список рубрик и возвращаем его в качестве  результата
'''