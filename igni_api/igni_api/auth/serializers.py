from hashlib import sha512
from rest_framework import serializers
from igni_api.core import models
from django.contrib.auth.hashers import check_password


class CompanyRegistrationSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     obj = models.Company.objects.create(**validated_data)
	# 	temp = dict()
	# 	temp['status'] = False
	# 	temp['message'] = "Company already exist."
    #     return obj

    class Meta:
        model = models.Company
        fields = ["org_name", "url"]


class UserRegistrationSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		email = self.validated_data['email']
		self.validated_data['username'] = email
		user = models.Users(**self.validated_data)
		has_rec = models.Users.objects.filter(username= email)
		if has_rec.count() > 0:
			return has_rec.count() , False
		user.set_password(user.password)
		user.save()
		return user ,True

	class Meta:
		model = models.Users
		fields = ('email', 'password', 'first_name', 'last_name','company')


class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(max_length=1000)

	def authenticate_create_token(self):
		# password = sha512(self.validated_data['password']).hexdigest()
		password = self.validated_data['password']
		user = models.Users.objects.filter(email=self.validated_data['email'])
		result = dict()
		if user.count() >= 1:
			user = user.get()
			if not user.is_verified:
				result['status'] = False
				result['is_verified'] = False
				result['error'] = "Email Not Verified."
				return result
			pass_status = check_password(password, user.password)
			if pass_status:
				token = models.Token(user=user).save()
				result['status'] = True
				result['token'] = token.key
				return result
			else:
				result['status'] = False
				result['error'] = "Invalid Credentials"
				return result
		else:
			result['status'] = False
			result['error'] = "Invalid Credentials"
			return result

class VerifyOTPSerializer(serializers.Serializer):
	verification_code = serializers.CharField(min_length=6)
	email = serializers.EmailField()
	class Meta:
		fields = ('verification_code' , 'email')

class GetOTPSerializer(serializers.Serializer):
	email = serializers.EmailField()
	class Meta:
		model = models.Users
		fields =  ('email',)


class RequestForgetPasswordSerializer(serializers.Serializer):
	email = serializers.EmailField()

	class Meta:
		fields = '__all__'

class ForgetPasswordSerializer(serializers.Serializer):
	email = serializers.EmailField()
	key = serializers.CharField(max_length=40)
	new_password = serializers.CharField()

	class Meta:
		fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Users
		fields = ['first_name', 'last_name', 'username', 'display_picture']