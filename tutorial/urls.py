from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views as quickstart_views

# Quickstart 用 router
router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Quickstart API
    path('api/', include(router.urls)),

    # Tutorial 5 API
    path('', include('snippets.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]