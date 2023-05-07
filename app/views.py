from django.db.models import Q

from rest_framework import generics
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models
from . import serializers


class FilmWorkListAPIView(generics.ListAPIView):
    """
    FilmWork List and Create View
    :param limit: int
    """
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkSerializer


class RatingListAPIView(generics.ListAPIView):
    """
    Rating List View
    :param limit: int
    """
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class GenreListAPIView(generics.ListAPIView):
    """
    Genre List View
    :param limit: int
    """
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class PersonListAPIView(generics.ListAPIView):
    """
    Person List View
    :param limit: int
    """
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class CurrencyListAPIView(generics.ListAPIView):
    """
    Currency List View
    :param limit: int
    """
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencySerializer


class FilmWorkRetrieveAPIView(views.APIView):
    """
    FilmWork Retrieve View
    """
    def get(self, request, pk, *args, **kwargs):
        serializer = serializers.FilmWorkSerializer(instance=get_object_or_404(models.FilmWork, pk=pk))
        return Response(serializer.data)


class FilmWorkListNewMovieAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.filter(type='movie').order_by('-premiere')
    serializer_class = serializers.FilmWorkSerializer


class FilmWorkListFamilyMovieAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.filter(type='movie', genres__name__exact='Семейные')
    serializer_class = serializers.FilmWorkSerializer


class FilmWorkListHorrorMovieAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.filter(type='movie', genres__name__exact='Ужасы')
    serializer_class = serializers.FilmWorkSerializer


class FilmWorkListNewCartoonAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.filter(type='cartoon').order_by('-premiere')
    serializer_class = serializers.FilmWorkSerializer


class FilmWorkListFamilyCartoonAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.filter(type='cartoon', genres__name__exact='Семейные')
    serializer_class = serializers.FilmWorkSerializer


class FilmWorkListHorrorCartoonAPIView(generics.ListAPIView):
    queryset = models.FilmWork.objects.filter(type='cartoon', genres__name__exact='Ужасы')
    serializer_class = serializers.FilmWorkSerializer


class FilmWorkListMovieCartoonNew(generics.ListAPIView):

    serializer_class = serializers.FilmWorkSerializer

    def get_queryset(self):
        movies = models.FilmWork.objects.filter(type='movie').order_by('-premiere')[:7]
        cartoons = models.FilmWork.objects.filter(type='cartoon').order_by('-premiere')[:7]
        return movies | cartoons


class FilmWorkListMovieCartoonHorror(generics.ListAPIView):

    serializer_class = serializers.FilmWorkSerializer

    def get_queryset(self):
        movies = models.FilmWork.objects.filter(type='movie', genres__name='ужасы')[:7]
        cartoons = models.FilmWork.objects.filter(type='cartoon', genres__name='ужасы')[:7]
        return movies | cartoons


class FilmWorkListMovieCartoonFamily(generics.ListAPIView):
    serializer_class = serializers.FilmWorkSerializer

    def get_queryset(self):
        movies = models.FilmWork.objects.filter(type='movie', genres__name='семейный')[:7]
        cartoons = models.FilmWork.objects.filter(type='cartoon', genres__name='семейный')[:7]
        return movies | cartoons
