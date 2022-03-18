from django.shortcuts import render, redirect


def home(request):
    context = {}
    return render(request, 'account/main.html', context)
