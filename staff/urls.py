from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StaffViewset


router = DefaultRouter()
router.register('', StaffViewset, basename='staff')

urlpatterns = [
    path('staff/', include(router.urls))
]
