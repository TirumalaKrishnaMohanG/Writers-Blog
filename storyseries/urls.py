from . import views
from django.urls import path
from django.urls import include
from .router import router


urlpatterns = [
    path('home',views.home,name='home'),
    path('write',views.write,name='write'),
    path('writemod',views.writemod,name='written'),
    #path('seenstory/<int:id>/',views.seenstory,name='seenstory'),
    path('seenstory/<int:id>/',views.seenstory,name='seenstory'),
    path('comment',views.comment,name='comment'),
    path('api/',include(router.urls))
]