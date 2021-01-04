from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# user_signup = UserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', views.UserViewSet.as_view()),
    path('users/employees/', views.EmployeeViewSet.as_view()),
    path('jobs/', views.JobViewSet.as_view()),
    path('jobs/<int:pk>/', views.JobDetail.as_view()),
    path('applications/', views.ApplicationViewSet.as_view()),
    # path('rest-auth/',  include('rest_auth.urls')),
    # path('rest-auth/registration/',include('rest_auth.registration.urls'))
     
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)