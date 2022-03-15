from django.urls import path
from clean_city.views import *


urlpatterns = [
    path('signup/admin/', AdminSignup.as_view(), name='signup'),
    path('login/', SigninApiView.as_view(), name='login'),
    path('register/staff/', RegisterStaffView.as_view(), name='register_staff'),
    path('password/forgot/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('password/reset/<str:email>',
         PasswordResetAPIView.as_view(), name='password-reset'),
    path('task/get_user_task/', GetUserTaskView.as_view(), name='get_task'),
    path('admin/view/all_users', AdminViewAllUsersAPIView.as_view(),
         name='admin-view-users'),
    path('profile/update/', EditProfileApiView.as_view(), name='profile-update'),
    path('task/accept/<int:id>/accept_task=<str:bool>',
         AcceptTask.as_view(), name='accept-task'),
    path('task/create', CreateTaskApiView.as_view(), name="create-task"),
    path('task/update/<int:pk>/', UpdateTaskApiView.as_view(), name="task-update"),
    path('get_cleaners_and_bin_collectors/', GetCleanersAndBinCollectorsAPIView.as_view(),
         name="get-cleaners-and-bin-collectors"),
    path('deactivate/<int:pk>/', DeactivateUserAPIView.as_view(),
         name="deactivate-user"),
]
