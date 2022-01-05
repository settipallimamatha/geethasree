from rest_framework.serializers import ModelSerializer
from.models import klmn
class klmnSerializer(ModelSerializer):
    class Meta:
        model=klmn
        fields=['name', 'costperitem', 'stockquantity', 'volume']