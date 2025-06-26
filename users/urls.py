from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    SendFriendRequestView,
    PendingFriendRequestsView,
    AcceptFriendRequestView,
    FriendsListView,
    HangoutEventListView,
    CreateHangoutEventView,
    DeleteHangoutEventView
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('friend-request/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend-request/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
    path('friend-request/<int:pk>/accept/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('friends/', FriendsListView.as_view(), name='friend-list'),
    path('hangouts/', HangoutEventListView.as_view(), name='hangout-list'),
    path('hangouts/create/', CreateHangoutEventView.as_view(), name='create-hangout'),
    path('hangouts/<int:pk>/delete/', DeleteHangoutEventView.as_view(), name='delete-hangout'),
]
