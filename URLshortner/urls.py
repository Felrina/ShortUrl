from django.contrib import admin
from django.urls import path, include
from shortner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BaseView.as_view(), name='BaseView'),
    path('', include('shortner.urls')),
]
