from django.urls import path,include
from .views import *
from .router import router

urlpatterns = [
    path("tanlovlar/",Api_Tanlovlar),
    # path("tanlov/",Api_Tanlov),
    path("login/",Api_Login),

    path("",include(router.urls)),

]
