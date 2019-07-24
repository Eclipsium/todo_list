from django.urls import path

from user_api.views import CurrentUser, InviteUser

urlpatterns = [
    path('<int:pk>/', CurrentUser.as_view()),
    path('invite/', InviteUser.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),

]
