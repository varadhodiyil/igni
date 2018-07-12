from django.conf.urls import url
from igni_api.core import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^device/$' , views.DeviceAPI.as_view()),
    url(r'^device/(?P<device>\d)/$' , views.DeviceUpdateAPI.as_view()),
    url(r'^device/logs/$' , views.DeviceLogsAPI.as_view()),
    url(r'^device/logs/(?P<device>\d)/$' , views.DeviceLogsUpdateAPI.as_view()),
    url(r'^dashboard/$' , views.Dashboard.as_view()),
    url(r'^report/vehicle/$' , views.VehicleReportAPI.as_view())
]
