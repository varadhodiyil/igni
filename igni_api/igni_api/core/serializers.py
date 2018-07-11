from rest_framework import serializers
from igni_api.core import models
from django.db.models import Max
class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Device
		fields = '__all__'


class DeviceLogsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.DeviceLogs
		fields = '__all__'

class DashBoardSerializer(serializers.ModelSerializer):
	def to_representation(self,instance):
		data = super(DashBoardSerializer, self).to_representation(instance)
		latest_date = models.DeviceLogs.objects.filter(device=instance.id)
		if latest_date.count() > 0:
			latest_date = latest_date.latest('updated_at')
			data.update(DeviceLogsSerializer(latest_date).data)
		return data

	class Meta:
		model = models.Device
		fields = '__all__'

class VehicleFilterSerializer(serializers.Serializer):
	start_date = serializers.DateTimeField(required=False)
	end_date = serializers.DateTimeField(required=False)
	device_id = serializers.IntegerField(required=False)