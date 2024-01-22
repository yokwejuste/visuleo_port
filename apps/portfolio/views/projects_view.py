from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from models import Projects, Categories
from serializers import ProjectsSerializer, ProjectsResponseSerializer
from utils import load_document
from paginators import ProjectsPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    pagination_class = ProjectsPagination
    parser_classes = [MultiPartParser, FormParser]
    filterset_fields = ["category", "tags", "is_published"]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Projects.objects.all()
        else:
            return Projects.objects.filter(is_featured=True)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        search = request.query_params.get("search")
        if search is not None:
            queryset = queryset.filter(name__icontains=search)
        id = request.query_params.get("id")
        if id is not None:
            queryset = queryset.filter(id=id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProjectsResponseSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProjectsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        categories = request.data.pop("categories")
        for category in categories:
            category, _ = Categories.objects.get_or_create(**category)
            Categories.objects.get_or_create(**category)
        serializer = ProjectsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
