from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('rahbarlar', RahbarlarViewSet)
router.register('ishlar', IshlarViewSet)
router.register('ariza',ArizaViewSet)