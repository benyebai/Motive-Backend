from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    SendFriendRequestView,
    PendingFriendRequestsView,
    AcceptFriendRequestView,
    FriendsListView
)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/friend-request/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('api/friend-request/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
    path('api/friend-request/<int:pk>/accept/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('api/friends/', FriendsListView.as_view(), name='friend-list'),
]
