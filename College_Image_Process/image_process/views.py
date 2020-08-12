from django.shortcuts import render
from django.http import HttpResponse
import os
def index(request):
    # return HttpResponse("hey"+os.getcwd())
    return HttpResponse("hey ram")