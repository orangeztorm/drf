from django.shortcuts import render
from django.http import JsonResponse

# Create your apis here.

def api_home(request, **args,):
    return JsonResponse({
        'message': 'hi there first django api'
    })

