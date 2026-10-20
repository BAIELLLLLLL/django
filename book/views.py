from django.http import HttpResponse


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