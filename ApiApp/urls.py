from django.urls import path,include
from .views import *
from .router import router

urlpatterns = [
    path("login/",Api_Login),
    path("tanlovlar/",Api_Tanlovlar),
    # path("tanlovlar/",Api_Tanlov),

    path("",include(router.urls)),

]
