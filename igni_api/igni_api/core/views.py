# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response

from igni_api.core import models, serializers

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


	def put(self, request, log, *args, **kwargs):
		user = request.user
		result = dict()
		if user.is_authenticated():
			result['status'] = True
			data = request.data
			data['owner'] = user.company.id
			instance = models.DeviceLogs.objects.filter(device__owner=user.company, id=log)
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
			data = models.Device.objects.filter(device__owner=user.company, id=device).delete()
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
			data = models.Device.objects.filter(device__owner=user.company, id=device)
			data = get_object_or_404(data)
			result['result'] = self.get_serializer(data).data
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
