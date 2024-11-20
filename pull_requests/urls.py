from django.urls import path
from .views import PullRequestListCreateView, PullRequestDetailView

urlpatterns = [
    path('', PullRequestListCreateView.as_view(), name='pull_request_list_create'),
    path('<int:pk>/', PullRequestDetailView.as_view(), name='pull_request_detail')
]