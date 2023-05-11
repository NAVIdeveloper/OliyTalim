from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('rahbarlar', RahbarlarViewSet)
router.register('ishlar', IshlarViewSet)
router.register('ariza',ArizaViewSet)
router.register('news',NewViewSet)
router.register("hududlar",HududlarViewSet)
