from django.urls import path

from user_api.views import DetailUser, InviteUser, CurrentUser, CreateUser

urlpatterns = [
    path('', CurrentUser.as_view()),
    path('detail/<int:pk>/', DetailUser.as_view()),
    path('invite/', InviteUser.as_view()),
    path('create/', CreateUser.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),

]
