
from django.urls import path
from .views import (
    HomePageView,
    RandomChartData
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('chart/', RandomChartData.as_view(), name='random-chart')
]
