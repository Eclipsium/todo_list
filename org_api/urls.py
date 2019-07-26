from django.urls import path

from org_api.views import *

urlpatterns = [
    path('', AccessibleOrganizations.as_view()),
    path('create/', CreateOrganization.as_view()),
    path('detail/<int:pk>/', DetailOrganization.as_view()),
    # path('invite/', UserInvite.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),

]
