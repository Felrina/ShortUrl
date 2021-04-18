from django.urls import path
from shortner import views

app_name = 'shortner'

urlpatterns = [
    path('', views.BaseView.as_view(), name='BaseView'),
    path('<short_url>', views.URLRedirectView.as_view(), name='URLRedirectView'),
]