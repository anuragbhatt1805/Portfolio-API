from rest_framework import viewsets
from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer, FeedbackSerializerData
from feedback.permission import ViewFeedback

# Create your views here.
class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (ViewFeedback,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FeedbackSerializer
        else:
            return FeedbackSerializerData

    def get_queryset(self):
        if self.action == 'list':
            return []