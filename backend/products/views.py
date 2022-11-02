from re import A
from rest_framework import generics, mixins, permissions, authentication

from .permissions import IsStaffEditorPermission

from .models import Product

from .serializers import ProductSerializer

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from django.http import Http404


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    # it gets called only on only the createApiView
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send a signal
        # return super().perform_create(serializer)


product_list_create_view = ProductListCreateApiView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        # instance
        return super().perform_destroy(instance)


product_delete_detail_view = ProductDeleteAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

        # return super().perform_update(serializer)


product_update_view = ProductUpdateAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


# function based view

# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             # get request -> details view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)

#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         # create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')  # type: ignore
#             content = serializer.validated_data.get('content') or None  # type: ignore
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_mixin_view = ProductMixinView.as_view()
