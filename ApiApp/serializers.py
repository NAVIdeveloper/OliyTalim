from .models import *
from rest_framework.serializers import ModelSerializer,SerializerMethodField


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
        
class LoaderBaholashMezon(ModelSerializer):
    class Meta:
        model = BaholashMezon
        fields = "__all__"

class LoaderBaholash(ModelSerializer):
    umumiy = SerializerMethodField()
    def get_umumiy(self,obj):
        total = obj.oquv_ishlari+obj.yoshlar+obj.ishlab_chiqarish+obj.moliyaviy+obj.xojalik+obj.talim_sifati+obj.ijro_intizomi
        total -= obj.jazo
        return total
    class Meta:
        model = Baholash
        fields = "__all__"