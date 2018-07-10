from igni_api.auth.serializers import CompanyRegistrationSerializer, UserRegistrationSerializer
from igni_api.core.models import Company


def get_register_company(data):
    response = dict()
    data = data.copy()
    company_serializer = CompanyRegistrationSerializer(data=data)
    if company_serializer.is_valid():
		company_obj = company_serializer.save()
		data['company'] = company_obj.id
		user_serializer = UserRegistrationSerializer(data=data)
		if user_serializer.is_valid():
			user_serializer.save()
			
			response['status'] = True
			# update_logs(str(company_obj.org_name),"COMPANY REGISTER", "New company registration.")
		else:
			Company.objects.filter(id=company_obj.id).delete()
			response['status'] = False
			response['message'] = user_serializer.errors
    else:
        response['status'] = False
        response['message'] = company_serializer.errors
    return response
