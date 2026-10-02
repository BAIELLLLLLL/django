from django.shortcuts import render
from django.http import HttpResponse


def hello_world_views(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World!")

def my_favourite_emodji_views(request):
    if request.method == 'GET':
        return HttpResponse("😎🤖")

def about_my_self_views(request):
    if request.method == 'GET':
        return HttpResponse("My name is Baiel, I am 17 years old, I am from Kyrgyzstan, I am a student of the 11th grade, I like programming and football, my favourite football team is Real Madrid, my favourite football player is Ronaldo, my favourite programming language is Python, my favourite framework is Django.")
    
