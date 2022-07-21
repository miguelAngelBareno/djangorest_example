from django.urls import path
from apps.users.api.api import UserAPIView, user_decorator_api_view, user_detail_view

urlpatterns = [
    path("viewUsuario/",UserAPIView.as_view(), name = 'usuario_api'),
    path("viewDecoratorUsuario/",user_decorator_api_view, name = 'usuario_decorator_api'),
    path("viewDecoratorUsuario/<int:pk>/",user_detail_view, name ='usuario_detail_api'),
]
