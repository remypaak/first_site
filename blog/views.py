from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("HOI")


def posts(request):
    return HttpResponse("HOIHOI")


def specific_post(request, post_name: str):
    return HttpResponse(post_name)



