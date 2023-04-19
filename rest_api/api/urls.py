from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import EducationalViewSet

router = SimpleRouter()
router.register('educational', EducationalViewSet)

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
