from django.urls import path, include
from Rest_Api.views import *

urlpatterns = [
    path('org/', CurrentOrganizations.as_view()),
    path('user/', CurrentUser.as_view()),
    path('user/invite/', UserInvite.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),

]
