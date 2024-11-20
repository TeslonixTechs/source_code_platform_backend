from django.urls import path
from .views import IssueListCreateView, IssueDetailView

urlpatterns = [
    path('', IssueListCreateView.as_view(), name='issue_list_create'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue_detail')
]