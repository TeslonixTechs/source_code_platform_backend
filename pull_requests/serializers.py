from rest_framework import serializers
from .models import Repository
from .models import PullRequest

class PullRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequest
        fields = ['id', 'title', 'description', 'creator', 'created_at', 'updated_at', 'status']