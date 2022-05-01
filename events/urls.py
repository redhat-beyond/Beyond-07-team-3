from . import views
from django.urls import path


urlpatterns = [
    path("create/", views.create_event, name="create_event"),
    path('meeting_vote/', views.meeting_vote, name='meeting_vote'),
    path('update/<str:event_id>', views.update_event, name='update_event'),
    path("meeting/", views.CreateMeetingView.as_view(), name="create_meeting"),
    path('remove_participant/',
         views.remove_participant_from_meeting, name='remove_participant'),
]
