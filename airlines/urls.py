from django.urls import path
from .views import (
    AirlineListCreateView,
    AirlineRetrieveUpdateDestroyView,
    AircraftListCreateView,
    AircraftRetrieveUpdateDestroyView,
    TestTokenView,
  
)
from .views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('airline/', AirlineListCreateView.as_view(), name='airline-list-create'),
    path('airline/<int:pk>/', AirlineRetrieveUpdateDestroyView.as_view(), name='airline-detail'),
    path('aircraft/', AircraftListCreateView.as_view(), name='aircraft-list-create'),
    path('aircraft/<int:pk>/', AircraftRetrieveUpdateDestroyView.as_view(), name='aircraft-detail'),
    path('test-token/', TestTokenView.as_view(), name='test_token'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]