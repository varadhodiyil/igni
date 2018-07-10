from django.conf.urls import url
from igni_api.auth import views

urlpatterns = [
	url(r'^register/org$', views.OrganizationRegister.as_view(), name="register_org"),
	url(r'^register/$', views.UserRegistration.as_view(), name="register"),
	url(r'^login/$', views.UserLogin.as_view(), name="login"),
	url(r'^request_password/$', views.RequestForgotPassword.as_view()),
	url(r'^forgot_password/$', views.ForgotPassword.as_view()),
	url(r'^profile/$', views.Profile.as_view()),
]