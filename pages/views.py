from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    my_text = {"location_context": ""}
    return render(request, "pages/index.html", context=my_text)


def indexfa(request):

    my_text = {"location_context": ""}
    return render(request, "pages/indexfa.html", context=my_text)
