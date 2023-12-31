from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, \
    MeasurementCreateAPIView, MeasurementRetrieveUpdateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor-retrieve-update'),
    path('measurements/', MeasurementCreateAPIView.as_view(), name='measurement-create'),
    path('measurements/<int:pk>/', MeasurementRetrieveUpdateAPIView.as_view(), name='measurement-retrieve-update'),
]