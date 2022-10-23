import json
from django.shortcuts import render
from django.http import JsonResponse
from products.serializers import ProductSerializer
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your apis here.


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
 
    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        data = ProductSerializer(instance).data

    return Response(data)
