from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, FestivalViewSet, GreetingViewSet, QuotationViewSet, LoginView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'festivals', FestivalViewSet)
router.register(r'greetings', GreetingViewSet)
router.register(r'quotations', QuotationViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Login URL
    path('', include(router.urls)),  # Include the router's URLs
]
