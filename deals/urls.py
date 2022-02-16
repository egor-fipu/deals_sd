from django.urls import path

from .views import DealsAPIView

urlpatterns = [
    path('v1/deals/', DealsAPIView.as_view()),
]
