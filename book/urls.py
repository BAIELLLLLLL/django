from django.urls import path
from . import views

urlpatterns = [
    path('favourite-writer/', views.my_favourite_writer),
    path('facts/', views.facts_about_writer),
    path('opinion/', views.my_opinion_about_writer),

    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
]
