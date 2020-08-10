from rest_framework.serializers import ModelSerializer

from smcrm.developers.models import Developer


class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = ['name', 'productivity']
