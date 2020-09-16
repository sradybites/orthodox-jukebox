from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    four = 2 + 2

    return render(
        request,
        "OrthodoxJukeboxApp/index.html",
        {
            'title': "A Page",
            'message': "2 plus 2 equals ",
            'content': four
        }
    )