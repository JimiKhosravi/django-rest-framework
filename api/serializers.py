from rest_framework import serializers
from api.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields = ("name", "age")
        fields = "__all__"
