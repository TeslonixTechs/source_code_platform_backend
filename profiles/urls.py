from django.urls import path
from .views import UserProfileDetailView

urlpatterns = [
    path('<int:pk>/', UserProfileDetailView.as_view(), name='user_profile_detail')
]