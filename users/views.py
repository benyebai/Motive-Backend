from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q

from .models import FriendRequest, Friendship, HangoutEvent
from .serializers import (
    CustomTokenObtainPairSerializer,
    FriendRequestSerializer,
    FriendshipSerializer,
    HangoutEventSerializer
)

# ✅ Custom login view
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# ✅ Send friend request
class SendFriendRequestView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendRequestSerializer

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

# ✅ View incoming friend requests
class PendingFriendRequestsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user)

# ✅ Accept a friend request
class AcceptFriendRequestView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()

        if friend_request.to_user != request.user:
            return Response({'error': 'Not authorized'}, status=403)

        Friendship.objects.create(user1=friend_request.from_user, user2=friend_request.to_user)
        friend_request.delete()

        return Response({'message': 'Friend request accepted.'})

# ✅ Get confirmed friends
class FriendsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendshipSerializer

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(Q(user1=user) | Q(user2=user))

# ✅ Get hangout events (user's own and friends')
class HangoutEventListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HangoutEventSerializer

    def get_queryset(self):
        user = self.request.user
        # Get user's friends
        friendships = Friendship.objects.filter(Q(user1=user) | Q(user2=user))
        friend_ids = []
        for friendship in friendships:
            if friendship.user1 == user:
                friend_ids.append(friendship.user2.id)
            else:
                friend_ids.append(friendship.user1.id)
        
        # Return events created by user or their friends
        return HangoutEvent.objects.filter(
            Q(created_by=user) | Q(created_by__id__in=friend_ids)
        ).order_by('-created_at')

# ✅ Create hangout event
class CreateHangoutEventView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HangoutEventSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
