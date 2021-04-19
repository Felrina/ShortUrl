from django.contrib import admin
from django.urls import path, include
from shortner import views, viewsets


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BaseView.as_view(), name='BaseView'),
    path('', include('shortner.urls')),
    path('urls/', viewsets.URL_objects.as_view()),
    path('urls/<int:pk>/', viewsets.URL_objects_details.as_view()),
]
