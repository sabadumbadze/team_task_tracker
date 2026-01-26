from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import 



router = DefaultRouter()
router.register(r'/health/', )
router.register(r'/about/', )
router.register(r'/forbidden/', )



urlpatterns = [
    path('', include(router.urls))
]
