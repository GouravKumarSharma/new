
from django.contrib import admin
from django.urls import path,include
from app import views,urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('',include('app.urls'),name='forum'),
    
    #path('Forum/'include('urls'))
]
