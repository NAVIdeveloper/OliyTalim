from django.urls import path,include
from .views import *
from .router import router

urlpatterns = [
    path("login/",Api_Login),
    path("tanlovlar/",Api_Tanlovlar),
    # path("tanlov/",Api_Tanlov),

    path("",include(router.urls)),

]
