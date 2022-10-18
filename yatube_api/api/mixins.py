from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class CreateListViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    pass
