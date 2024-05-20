from django.contrib import admin
from django.urls import path
from app.views import *

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="API documentation for my Django project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('statistics',StatisticsApiView.as_view()),
    path('sponsor/add',SponsorCreateView.as_view()),
    path('student/add',StudentCreateView.as_view()),
    path('list/sponsor/', SponsorApiView.as_view()),
    path('list/student', StudentApiView.as_view()),
    path('sponsor/<id>',SingleSponsorApi.as_view()),
    path('student/<id>',SingleStudentApi.as_view()),
    path('sponsor/<id>/update',SponsorUpdateView.as_view()),
    path('student/<id>/update',StudentUpdateView.as_view()),
    path('sponsor/<id>/delete',SponsorDeleteApiView.as_view()),
    path('student/<id>/delete',StudentDeleteApiView.as_view()),
    path('student/<id>/addSponsor/',SponsorshipCreateApiView.as_view()),
    path('student/<id>/sponsorship',StudentSponsorView.as_view()),
    path('search/', CombinedSearchApiView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]