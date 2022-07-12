from wowapp.views import RegisterAPI, LoginAPI
from django.urls import path, include
from knox import views as knox_views
from wowapp import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('descriptions', views.DescriptionViewSet)


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/weather/', include(router.urls)),
        
]
