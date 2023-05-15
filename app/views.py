from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import views
from rest_framework import filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from . import models
from . import serializers


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
        serializer = serializers.FilmWorkSerializer(instance=get_object_or_404(models.FilmWork, pk=pk))
        return Response(serializer.data)


class FilmWorkListFirstSlider(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkFirstSliderSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', ]
    ordering_fields = ['premiere', ]


class FilmWorkListOtherSlider(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkOtherSlidersSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', 'genres__name']
    ordering_fields = ['premiere', ]


class FilmWorkSearchAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class BrowsingHistoryCreateAPIView(generics.CreateAPIView):
    queryset = models.BrowsingHistory.objects.all()
    serializer_class = serializers.BrowsingHistorySerializer

    def perform_create(self, serializer):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        serializer.save(profile=profile, film_work_id=self.kwargs['pk'])


class FavoritesAddAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.FilmWorkSerializer(data=request.data)
        models.Profile.favorites.add(models.FilmWork.objects.get(id=serializer.data['id']))
        return Response(serializer.data, status=200)




