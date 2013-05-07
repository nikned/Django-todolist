from django.shortcuts import render_to_response

__author__ = 'nikh0881'

def index(request):
    # code...
    return render_to_response('index.html', locals())

def add(request):
    # code...
    return render_to_response('add.html', locals())

def delete(request):
    # code...
    return render_to_response('delete.html', locals())

def update(request):
    # code...
    return render_to_response('update.html', locals())
