from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.homePage, name='home'),
    # path('', views.ContactCreateView.as_view(), name='contact'),
    path('turnir_detail/<int:pk>/', views.turnir_detail, name='turnir_detail'),
    path('tadbir_detail/<int:pk>/', views.tadbir_detail, name='tadbir_detail'),
]