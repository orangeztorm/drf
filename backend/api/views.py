import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your apis here.


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}

    try:
        data = json.loads(body)
    except:
        pass

    print(data.keys());
    return JsonResponse(data)
