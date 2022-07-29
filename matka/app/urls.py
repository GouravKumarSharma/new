

from django.urls import path,include
from app import views,urls


urlpatterns = [
    path('',views.index,name="index"),
    path('JDForum/',views.jdforum,name="jdforum"),
    path('login/',views.login,name='login'),
    #path('Forum/'include('urls'))
]
