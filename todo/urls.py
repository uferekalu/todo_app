from django.urls import path
from .import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]