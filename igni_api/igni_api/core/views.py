# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response

from igni_api.core import models, serializers , resources

# Create your views here.


class DeviceAPI(GenericAPIView):
    serializer_class = serializers.DeviceSerializer
    parser_classes = (JSONParser, FormParser)

    def get(self, request, *args, **kwargs):
        user = request.user
        result = dict()
        if user.is_authenticated():
            result['status'] = True
            data = models.Device.objects.filter(owner=user.company)
            result['result'] = self.get_serializer(data, many=True).data
            return Response(result)
        else:
            result['status'] = False
            result['error'] = "Unauthorized"
            return Response(result, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        result = dict()
        if user.is_authenticated():
            data['owner'] = user.company.id
            s = self.get_serializer(data=data)
            if s.is_valid():
                s.save()
                result['status'] = True
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                result['status'] = False
                result['errors'] = s.errors
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
        else:
            result['status'] = False
            result['error'] = "Unauthorized"
            return Response(result, status=status.HTTP_401_UNAUTHORIZED)


class DeviceUpdateAPI(GenericAPIView):
	serializer_class = serializers.DeviceSerializer
	parser_classes = (JSONParser, FormParser)


	def put(self, request, device, *args, **kwargs):
		user = request.user
		result = dict()
		if user.is_authenticated():
			result['status'] = True
			data = request.data
			data['owner'] = user.company.id
			instance = models.Device.objects.filter(owner=user.company, id=device)
			instance = get_object_or_404(instance)
			s = self.get_serializer(instance, data=data)
			if s.is_valid():
				s.save()
				result['status'] = True
				return Response(result, status=status.HTTP_201_CREATED)
			else:
				result['status'] = False
				result['errors'] = s.errors
				return Response(result, status=status.HTTP_400_BAD_REQUEST)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)

	def delete(self, request, device, *args, **kwargs):
		user = request.user
		result = dict()
		if user.is_authenticated():
			result['status'] = True
			data = models.Device.objects.filter(owner=user.company, id=device).delete()
			result['result'] = data
			return Response(result)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)

	def get(self, request, device, *args, **kwargs):
		user = request.user
		result = dict()
		if user.is_authenticated():
			result['status'] = True
			data = models.Device.objects.filter(owner=user.company, id=device)
			data = get_object_or_404(data)
			result['result'] = self.get_serializer(data).data
			return Response(result)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)



class DeviceLogsAPI(GenericAPIView):
    serializer_class = serializers.DeviceLogsSerializer
    parser_classes = (JSONParser, FormParser)

    def get(self, request, *args, **kwargs):
        user = request.user
        result = dict()
        if user.is_authenticated():
            result['status'] = True
            data = models.DeviceLogs.objects.filter(device__owner=user.company)
            result['result'] = self.get_serializer(data, many=True).data
            return Response(result)
        else:
            result['status'] = False
            result['error'] = "Unauthorized"
            return Response(result, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        result = dict()
        if user.is_authenticated():
            data['owner'] = user.company.id
            s = self.get_serializer(data=data)
            if s.is_valid():
                s.save()
                result['status'] = True
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                result['status'] = False
                result['errors'] = s.errors
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
        else:
            result['status'] = False
            result['error'] = "Unauthorized"
            return Response(result, status=status.HTTP_401_UNAUTHORIZED)


class DeviceLogsUpdateAPI(GenericAPIView):
	serializer_class = serializers.DeviceLogsSerializer
	parser_classes = (JSONParser, FormParser)


	# def put(self, request, log, *args, **kwargs):
	# 	user = request.user
	# 	result = dict()
	# 	if user.is_authenticated():
	# 		result['status'] = True
	# 		data = request.data
	# 		data['owner'] = user.company.id
	# 		instance = models.DeviceLogs.objects.filter(device__owner=user.company, id=log)
	# 		instance = get_object_or_404(instance)
	# 		s = self.get_serializer(instance, data=data)
	# 		if s.is_valid():
	# 			s.save()
	# 			result['status'] = True
	# 			return Response(result, status=status.HTTP_201_CREATED)
	# 		else:
	# 			result['status'] = False
	# 			result['errors'] = s.errors
	# 			return Response(result, status=status.HTTP_400_BAD_REQUEST)
	# 	else:
	# 		result['status'] = False
	# 		result['error'] = "Unauthorized"
	# 		return Response(result, status=status.HTTP_401_UNAUTHORIZED)

	# def delete(self, request, log, *args, **kwargs):
	# 	user = request.user
	# 	result = dict()
	# 	if user.is_authenticated():
	# 		result['status'] = True
	# 		data = models.DeviceLogs.objects.filter(device__owner=user.company, id=log).delete()
	# 		result['result'] = data
	# 		return Response(result)
	# 	else:
	# 		result['status'] = False
	# 		result['error'] = "Unauthorized"
	# 		return Response(result, status=status.HTTP_401_UNAUTHORIZED)

	def get(self, request, device, *args, **kwargs):
		user = request.user
		result = dict()
		if user.is_authenticated():
			result['status'] = True
			data = models.DeviceLogs.objects.filter(device__owner=user.company, device=device)
			result['result'] = self.get_serializer(data,many=True).data
			return Response(result)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)


class Dashboard(GenericAPIView):

	serializer_class = serializers.DashBoardSerializer
	def get(self,request,*args,**kwargs):
		user = request.user
		result = dict()
		if user.is_authenticated():
			result['status'] = True
			data = models.Device.objects.filter(owner=user.company)
			result['result'] = self.get_serializer(data,many=True).data
			return Response(result)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)


class VehicleReportAPI(GenericAPIView):
	serializer_class = serializers.VehicleFilterSerializer

	def post(self,request,*args,**kwargs):
		user = request.user
		result = dict()
		if user.is_authenticated():
			
			s = self.get_serializer(data=request.data)
			if s.is_valid():
				result['status'] = True
				data = models.DeviceLogs.objects.filter(device__owner=user.company)
				if 'device_id' in s.validated_data:
					data = data.filter(device=s.validated_data['device_id'])
				if 'start_date' in s.validated_data and 'end_date' in s.validated_data:
					data = data.filter(updated_at__range=[s.validated_data['start_date'],\
						s.validated_data['end_date']])
				result['result'] = serializers.DeviceLogsSerializer(data,many=True).data
				return Response(result)
			else:
				result['status'] = False
				result['errors'] = s.errors
				return Response(result)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)

class DistanceReport(GenericAPIView):

	def get(self,request,*args, **kwargs):
		result = dict()
		user = request.user
		if user.is_authenticated():
			device = models.Device.objects.filter(owner=user.company)
			data = list()
			for d in device:
				co_ordinates = models.DeviceLogs.objects.filter(device=d).order_by("updated_at")
				_distance = 0
				max_length = co_ordinates.count()
				start_date = ''
				start_address = ''
				stop_address = ''
				stop_time = ''
				start_odometer = 0 
				stop_odometer = 0 
				for i, c in enumerate(co_ordinates):
					j = i + 1
					if i == 0 :
						start_date = c.updated_at
						start_address = c.address
						start_odometer = c.odometer
					if i == max_length -1 :
						j =i 
						stop_address =  c.address
						stop_time = c.updated_at
						stop_odometer = c.odometer
					source = c.latitude , c.longitude
					dest = co_ordinates[j].latitude , co_ordinates[j].longitude
					_distance += resources.distance(source,dest)
				d.distance = _distance
				d.description = d.name
				d.vehicle_id = d.id
				d.start_date = start_date
				d.start_address = start_address
				d.stop_address= stop_address
				d.stop_time = stop_time
				d.start_odometer = start_odometer
				d.stop_odometer = stop_odometer
				data.append(d)
			result['result'] = serializers.DistanceReportSerializer(data,many=True).data
			return Response(result)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)


class IgnitionReport(GenericAPIView):

	def get(self,request,*args, **kwargs):
		result = dict()
		user = request.user
		if user.is_authenticated():
			data = list()
			co_ordinates = models.DeviceLogs.objects.filter(device__owner=user.company).order_by("updated_at").prefetch_related('device')
			_distance = 0
			max_length = co_ordinates.count()
			start_date = ''
			start_address = ''
			stop_address = ''
			stop_time = ''
			start_odometer = 0 
			stop_odometer = 0 
			cnt = 0 
			start_status = ''
			start_lat  = None
			start_lng = None
			start_id = None
			for i, c in enumerate(co_ordinates):
				d = c.device
				
				if  c.ignition_status != start_status or (i == max_length -1 ):
					stop_address =  c.address
					stop_time = c.updated_at
					stop_odometer = c.odometer
					print c.ignition_status , start_status
					if start_lat is None:
						start_lat = c.latitude
					if start_lng is None:
						start_lng = c.longitude
					source = start_lat ,start_lng
					dest = c.latitude , c.longitude
					_distance += resources.distance(source,dest)
					d.distance = _distance
					d.description = d.name
					d.vehicle_id = d.id
					d.start_date = start_date
					d.start_address = start_address
					d.stop_address= stop_address
					d.stop_time = stop_time
					d.start_odometer = start_odometer
					d.stop_odometer = stop_odometer
					data.append(d)
					start_status = c.ignition_status


					start_date = c.updated_at
					start_address = c.address
					start_odometer = c.odometer
					start_lat = c.latitude
					start_lng =  c.longitude
					start_id = c.id
					

			result['result'] = serializers.DistanceReportSerializer(data,many=True).data
			return Response(result)
		else:
			result['status'] = False
			result['error'] = "Unauthorized"
			return Response(result, status=status.HTTP_401_UNAUTHORIZED)
