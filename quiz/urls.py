from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='quiz_index'),
    path('submit/', views.submit_answer, name='quiz_submit'),
]
