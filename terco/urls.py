from django.urls import path
from .views import TercoAPIView

urlpatterns = [
    path('terco/', TercoAPIView.as_view(), name='terco_api'),
]