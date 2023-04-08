from django.shortcuts import render

# Create your views here.


def faq(request):
    context = {}
    template = "faq/faq.html"
    return render(request, template, context)
