
from django.urls import path
from .views import home, toggle_todo, delete_todo

urlpatterns = [
    path('', home, name='home'),
    path('toggle/<int:todo_id>/', toggle_todo, name='toggle_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]
