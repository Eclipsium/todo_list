from django.urls import path
from todo_api.views import *

urlpatterns = [

    path('', TaskList.as_view()),
    path('detail/<int:pk>/', TaskListDetail.as_view()),
    path('create/', CreateTask.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),

]
