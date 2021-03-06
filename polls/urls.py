"""from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<str:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<str:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='polls:index'),
    path('<int:pk>/', views.DetailView.as_view(), name='polls:detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='polls:results'),
    path('<int:question_id>/vote/', views.vote, name='polls:vote'),
]