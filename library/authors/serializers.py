from rest_framework.serializers import HyperlinkedModelSerializer

from.models import Author

class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Authorfields = "__all__"
