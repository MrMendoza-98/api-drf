from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloWorldViewSet, basename = 'hello-viewset')
router.register(r'profile', views.UserProfileViewSet)
router.register(r'feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloWorldAPIView.as_view()),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]