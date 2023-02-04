from django.urls import path

from .views import index, by_rubric, BbCreateView


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    # в вызов функции path() подставляется результат, возвращенный методом as_view() контроллера-класса

    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]