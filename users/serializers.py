from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import FriendRequest, Friendship, HangoutEvent

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return {
            'token': data['access']
        }

class FriendRequestSerializer(serializers.ModelSerializer):
    # read only just means, only use this when its sent out to the client
    # ignore it if the user sends it
    from_user_username = serializers.CharField(source='from_user.username', read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'timestamp', 'from_user_username']
        read_only_fields = ['from_user', 'timestamp', 'to_user']

class FriendshipSerializer(serializers.ModelSerializer):
    friend_username = serializers.SerializerMethodField()

    class Meta:
        model = Friendship
        fields = ['id', 'friend_username', 'created_at']

    def get_friend_username(self, obj):
        request_user = self.context['request'].user
        if obj.user1 == request_user:
            return obj.user2.username
        return obj.user1.username

class HangoutEventSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    date_time = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S.%fZ')
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S.%fZ', read_only=True)

    class Meta:
        model = HangoutEvent
        fields = ['id', 'title', 'description', 'attendee_count', 'date_time', 'created_by', 'created_at']
        read_only_fields = ['id', 'created_by', 'created_at']
