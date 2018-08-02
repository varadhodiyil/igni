from django.db.models import Max
from rest_framework import serializers
from django.utils import timesince
from igni_api.core import models


class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Device
		fields = '__all__'


class DeviceLogsSerializer(serializers.ModelSerializer):
	def to_representation(self,instance):
		data = super(DeviceLogsSerializer, self).to_representation(instance)
		data['device_name'] = instance.device.name
		return data
	class Meta:
		model = models.DeviceLogs
		fields = '__all__'

class DashBoardSerializer(serializers.ModelSerializer):
	def to_representation(self,instance):
		data = super(DashBoardSerializer, self).to_representation(instance)
		latest_date = models.DeviceLogs.objects.filter(device=instance.id)
		
		if latest_date.count() > 0:
			latest_date = latest_date.latest('updated_at')
			latest_date.updated_at = timesince.timesince(latest_date.updated_at) + " ago"
			data.update(DeviceLogsSerializer(latest_date).data)
		if 'ac_status' in data:
			data['ac_status'] = data['ac_status'].lower()
		return data

	class Meta:
		model = models.Device
		fields = '__all__'

class VehicleFilterSerializer(serializers.Serializer):
	start_date = serializers.DateTimeField(required=False)
	end_date = serializers.DateTimeField(required=False)
	device_id = serializers.IntegerField(required=False)


class DistanceReportSerializer(serializers.Serializer):
	description = serializers.CharField()
	vehicle_id = serializers.IntegerField()
	start_date = serializers.DateTimeField()
	stop_time = serializers.DateTimeField()
	start_address = serializers.CharField()
	stop_address = serializers.CharField()
	start_odometer = serializers.IntegerField()
	stop_odometer = serializers.IntegerField()
	distance = serializers.FloatField()

	class Meta:
		fields = '__all__'
