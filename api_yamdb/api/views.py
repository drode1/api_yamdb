from api.serializers import CommentSerializer, ReviewSerializer
from rest_framework import viewsets
from reviews.models import Review, Title

from .permissions import IsAdminOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = Title.objects.get(pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = Title.objects.get(pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = Review.objects.get(
            pk=self.kwargs.get('review_id'),
            title__pk=self.kwargs.get('title_id')
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = Review.objects.get(
            pk=self.kwargs.get('review_id'),
            title__pk=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, review=review)
