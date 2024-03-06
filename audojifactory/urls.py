from django.urls import path
from audojifactory.views import TranscribeView

urlpatterns = [
    path('transcribe/', TranscribeView.as_view(), name='transcribe'),
]