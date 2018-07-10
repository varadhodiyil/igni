# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from hashlib import sha1

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response

from igni_api.auth import models, serializers , resources

class OrganizationRegister(GenericAPIView):
    serializer_class = serializers.CompanyRegistrationSerializer
    parser_classes = (JSONParser, FormParser)
    def post(self,request,*args,**kwargs):
        resp = resources.get_register_company(request.data)
        return Response(resp,status=status.HTTP_200_OK)

# Create your views here.
class UserRegistration(GenericAPIView):
    """ User Registration """
    serializer_class = serializers.UserRegistrationSerializer
    parser_classes = ((JSONParser, FormParser))

    def post(self, request, *args, **kwargs):
        data = request.data
        s = serializers.UserRegistrationSerializer(data=data)
        result = dict()
        if s.is_valid():
            instance, _status = s.save()
            if _status:
                #   
                instance.save()
                result['status'] = True
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                result['status'] = False
                result['error'] = "Hey , We checked our Records , A user with similar records already exits"
                return Response(result, status=status.HTTP_200_OK)
        else:
            result['status'] = False
            result['errors'] = s.errors
            return Response(result, status=status.HTTP_200_OK)


class UserLogin(GenericAPIView):
    """ User Login """
    serializer_class = serializers.UserLoginSerializer
    parser_classes = ((JSONParser, FormParser))

    def post(self, request, *args, **kwargs):
        s = serializers.UserLoginSerializer(data=request.data)
        result = dict()
        if s.is_valid():
            result = s.authenticate_create_token()
            return Response(result, status=status.HTTP_200_OK)
        else:
            result['status'] = False
            result['errors'] = s.errors
            return Response(result, status=status.HTTP_200_OK)




class RequestForgotPassword(GenericAPIView):

    serializer_class = serializers.RequestForgetPasswordSerializer
    parser_classes = ((JSONParser,))

    def post(self, request, *args, **kwargs):
        data = request.data
        s = serializers.RequestForgetPasswordSerializer(data=data)
        result = dict()
        if s.is_valid():
            email = s.validated_data['email']
            user = models.Users.objects.filter(email=email)
            user = get_object_or_404(user)
            _now = timezone.now()
            _code_meta = user.email + _now.strftime("%s")
            _hash = sha1(user.email + _code_meta).hexdigest()
            user.forget_pass_code = _hash
            user.forget_pass_code_validity = _now + \
                datetime.timedelta(minutes=15)
            user.save()
            result['status'] = True
            return Response(result)
        else:
            result['status'] = False
            result['errors'] = s.errors
            return Response(result, status=status.HTTP_400_BAD_REQUEST)


class ForgotPassword(GenericAPIView):

    serializer_class = serializers.ForgetPasswordSerializer
    parser_classes = ((JSONParser,))

    def post(self, request, *args, **kwargs):
        data = request.data
        s = serializers.ForgetPasswordSerializer(data=data)
        result = dict()
        if s.is_valid():
            email = s.validated_data['email']
            key = s.validated_data['key']
            password = s.validated_data['new_password']
            user = models.Users.objects.filter(
                email=email, forget_pass_code=key)
            user = get_object_or_404(user)
            if user.forget_pass_code_validity > timezone.now():
                user.forget_pass_code = None
                user.forget_pass_code_validity = None
                user.set_password(password)
                user.save()
                result['status'] = True
            else:
                result['status'] = False
                result['error'] = "Token Expired"
            return Response(result)
        else:
            result['status'] = False
            result['errors'] = s.errors
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

class Profile(GenericAPIView):
    """ Profile """
    serializer_class = serializers.ProfileSerializer

    def get(self, request, *Args, **kwargs):
        if request.user.is_authenticated():
            data = serializers.ProfileSerializer(request.user).data
            temp = dict()
            temp['status'] = True
            temp['result'] = data
            return Response(temp, status=status.HTTP_200_OK)
        else:
            temp = dict()
            temp['status'] = False
            temp['error'] = "Not Authorised"
            return Response(temp, status=status.HTTP_401_UNAUTHORIZED)