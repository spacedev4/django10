from django.contrib import admin
from django.urls import path
from .views import author_list
from .views import genre_list
from .views import book_list
from .views import alls

urlpatterns = [
    path('author_list/', author_list),
    path('genre_list/', genre_list),
    path('book_list/', book_list),
    path('alls/', alls)
]