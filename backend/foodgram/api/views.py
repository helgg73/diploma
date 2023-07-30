from rest_framework import filters, mixins, status, viewsets

from recipes.models import Tags
from api.serializers import TagsSerializer


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    pagination_class = None
