from django.contrib import admin
from django.urls import path
from . import views  # Pastikan ini merujuk pada views di aplikasi Anda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('key/', views.key, name='key'),  
    path('masak/', views.masak, name='masak'),
    path('tenis/', views.tenis, name='tenis'),
    path('gitar/', views.gitar, name='gitar'),
    
]
