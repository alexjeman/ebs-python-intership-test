from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import mixins

from apps.blog.models import Category, Blog
from apps.blog.serializers import CategorySerializer, BlogSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogDetail(
        mixins.RetrieveModelMixin,
        GenericAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
