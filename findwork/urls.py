from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', views.UserViewSet.as_view()),
    path('users/employees/', views.EmployeeViewSet.as_view()),
    path('jobs/', views.JobViewSet.as_view()),
    path('jobs/<int:pk>/', views.JobDetail.as_view()),
    path('applications/', views.ApplicationViewSet.as_view()),
     
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)