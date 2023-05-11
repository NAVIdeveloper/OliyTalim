from .models import *
from rest_framework.serializers import ModelSerializer


class LoaderRahbarlar(ModelSerializer):
    class Meta:
        model = Rahbarlar
        fields = "__all__"


class LoaderIshlar(ModelSerializer):
    class Meta:
        model = Ishlar
        fields = "__all__"


class LoaderAriza(ModelSerializer):
    class Meta:
        model = Ariza
        fields = "__all__"

class LoaderNew(ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"

class LoaderHududlar(ModelSerializer):
    class Meta:
        model = Hududlar
        fields = "__all__"
        