from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    html = """
        <h1>First page</h1>
        <a href="second/">Second page</a>
    """
    return HttpResponse(html)


def second(request):
    html = """
        <h1>Second page</h1>
        <a href="../">First page</a>
    """
    return HttpResponse(html)