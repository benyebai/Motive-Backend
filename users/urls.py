from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    SendFriendRequestView,
    PendingFriendRequestsView,
    AcceptFriendRequestView,
    FriendsListView,
    HangoutEventListView,
    CreateHangoutEventView
)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/friend-request/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('api/friend-request/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
    path('api/friend-request/<int:pk>/accept/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('api/friends/', FriendsListView.as_view(), name='friend-list'),
    path('api/hangouts/', HangoutEventListView.as_view(), name='hangout-list'),
    path('api/hangouts/create/', CreateHangoutEventView.as_view(), name='create-hangout'),
]
