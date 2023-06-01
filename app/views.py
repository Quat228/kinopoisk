from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import views
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from . import permissions


class FilmWorkListAPIView(generics.ListAPIView):
    """
    FilmWork List View
    """
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', 'genres__name']
    ordering_fields = ['premiere']


class RatingListAPIView(generics.ListAPIView):
    """
    Rating List View
    """
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    pagination_class = LimitOffsetPagination


class GenreListAPIView(generics.ListAPIView):
    """
    Genre List View
    """
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    pagination_class = LimitOffsetPagination


class PersonListAPIView(generics.ListAPIView):
    """
    Person List View
    """
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    pagination_class = LimitOffsetPagination


class CurrencyListAPIView(generics.ListAPIView):
    """
    Currency List View
    """
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencySerializer
    pagination_class = LimitOffsetPagination


class FilmWorkRetrieveAPIView(views.APIView):
    """
    FilmWork Retrieve View
    """
    def get(self, request, pk, *args, **kwargs):
        serializer = serializers.FilmWorkSerializer(
            instance=get_object_or_404(models.FilmWork, pk=pk),
            context={'request': request})
        return Response(serializer.data)


class FilmWorkListFirstSlider(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkFirstSliderSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', ]
    ordering_fields = ['premiere', ]


class FilmWorkFilterListAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkFilterSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', 'genres__name', 'year']
    ordering_fields = ['premiere', ]


class FilmWorkSearchAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class FilmWorkPopularListAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        sorted_queryset = sorted(super().get_queryset(), key=lambda filmwork: filmwork.get_views_count(), reverse=True)
        return sorted_queryset


class FilmWorkRecommendListAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        sorted_queryset = sorted(super().get_queryset(), key=lambda filmwork: filmwork.get_rating(), reverse=True)
        try:
            profile = get_object_or_404(models.Profile, user=self.request.user)
        except Exception as e:
            pass
        else:
            watched_genres_obj = \
                [history.film_work.genres.all().first() for history in profile.browsing_histories.all()]
            if watched_genres_obj:
                sorted_queryset = super().get_queryset().filter(genres__in=watched_genres_obj)
        finally:
            return sorted_queryset


class BrowsingHistoryCreateAPIView(generics.CreateAPIView):
    queryset = models.BrowsingHistory.objects.all()
    serializer_class = serializers.BrowsingHistorySerializer

    def perform_create(self, serializer):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        serializer.save(profile=profile, film_work_id=self.kwargs['pk'])


class FavoritesAddAPIView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        film_work = get_object_or_404(models.FilmWork, id=request.data['id'])
        if film_work in profile.favorites.all():
            profile.favorites.remove(film_work)
        else:
            profile.favorites.add(film_work)
        return Response(request.data, status=200)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthorOrIsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return super().get_queryset().filter(film_work_id=self.kwargs['film_work_id'])

    def perform_create(self, serializer):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        serializer.save(profile=profile, film_work_id=self.kwargs['film_work_id'])


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.ReadOnlyOrIsAuthor]

    def get_queryset(self):
        return super().get_queryset().filter(film_work_id=self.kwargs['film_work_id'])


class RatingCreateAPIView(generics.CreateAPIView):
    queryset = models.Rating
    serializer_class = serializers.RatingSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        serializer.save(profile=profile, film_work_id=self.kwargs['film_work_id'])


class FilmWorkReactionCreateAPIView(generics.CreateAPIView):
    queryset = models.FilmWorkReaction.objects.all()
    serializer_class = serializers.FilmWorkReactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        serializer.save(
            film_work=get_object_or_404(models.Comment, pk=self.kwargs['film_work_id']),
            profile=profile
        )


class CommentReactionCreateAPIView(generics.CreateAPIView):
    queryset = models.CommentReaction.objects.all()
    serializer_class = serializers.CommentReactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        serializer.save(
            comment=get_object_or_404(models.Comment, pk=self.kwargs['comment_id']),
            profile=profile
        )

