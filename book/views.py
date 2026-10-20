from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book



def my_favourite_writer(request):
    return HttpResponse("My favourite writer is Chingiz Aitmatov.")


def facts_about_writer(request):
    return HttpResponse(
        "Chingiz Aitmatov was a famous Kyrgyz writer. "
        "He wrote Jamila, The White Ship and "
        "The Day Lasts More Than a Hundred Years."
    )


def my_opinion_about_writer(request):
    return HttpResponse(
        "I think Chingiz Aitmatov is a great writer. "
        "His books teach us about love, kindness and humanity."
    )
def my_favourite_writer(request):
    return HttpResponse("My favourite writer is Chingiz Aitmatov.")


def facts_about_writer(request):
    return HttpResponse(
        "Chingiz Aitmatov was a famous Kyrgyz writer."
    )


def my_opinion_about_writer(request):
    return HttpResponse(
        "I think Chingiz Aitmatov is a great writer."
    )


def book_list(request):
    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'book/book_list.html', context)


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    context = {
        'book': book
    }

    return render(request, 'book/book_detail.html', context)