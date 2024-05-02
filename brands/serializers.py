from rest_framework.serializers import ModelSerializer
from brands.models import Brand


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'
