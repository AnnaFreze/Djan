from django.urls import path
from django.contrib import admin
from measurement.views import SensorView, MeasurementCreate, SensorDetail

urlpatterns = [
    path('sensors/',SensorView.as_view(), name='sensors'),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/info/<int:pk>', SensorDetail.as_view()),
    path('admin/', admin.site.urls),
]
