from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import (
    StatusAPIView,
    StatusListSearchAPIView,
    StatusCreateAPIView,
    StatusDetailAPIView,
    StatusDeleteAPIView,
    StatusUpdateAPIView
)
urlpatterns = [
    path('primary/', StatusAPIView.as_view()),
    path('2/', StatusListSearchAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    path('detail/<id>/', StatusDetailAPIView.as_view()),
    path('delete/<pk>', StatusDeleteAPIView.as_view()),
    path('update/<pk>', StatusUpdateAPIView),
    path('auth/jwt', obtain_jwt_token),
    path('auth/jwt/refresh', refresh_jwt_token)

]
