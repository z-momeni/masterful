from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context

def main(request):
    return render_to_response('main.html',{})
  