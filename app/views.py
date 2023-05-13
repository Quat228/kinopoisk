from rest_framework import generics
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from accounts import serializers as acc_serializer

from . import models
from . import serializers


class FilmWorkListAPIView(generics.ListAPIView):
    """
    FilmWork List View
    """
    queryset = models.FilmWork.objects.all()
    serializer_class = serializers.FilmWorkSerializer


class RatingListAPIView(generics.ListAPIView):
    """
    Rating List View
    """
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class GenreListAPIView(generics.ListAPIView):
    """
    Genre List View
    """
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class PersonListAPIView(generics.ListAPIView):
    """
    Person List View
    """
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class CurrencyListAPIView(generics.ListAPIView):
    """
    Currency List View
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
    """
    FilmWork List of new movies
    """
    queryset = models.FilmWork.objects.filter(type='movie').order_by('-premiere')
    serializer_class = serializers.FilmWorkFirstSliderSerializer


class FilmWorkListNewCartoonAPIView(generics.ListAPIView):
    """
    FilmWork list of new cartoon
    """
    queryset = models.FilmWork.objects.filter(type='cartoon').order_by('-premiere')[:14]
    serializer_class = serializers.FilmWorkFirstSliderSerializer


class FilmWorkListMovieCartoonNew(generics.ListAPIView):
    """
    FilmWork list of new movie and cartoon
    """

    serializer_class = serializers.FilmWorkFirstSliderSerializer

    def get_queryset(self):
        movies = models.FilmWork.objects.filter(type='movie').order_by('-premiere')[:7]
        cartoons = models.FilmWork.objects.filter(type='cartoon').order_by('-premiere')[:7]
        return movies | cartoons


class FilmWorkListMovieCartoonHorror(generics.ListAPIView):
    """
    FilmWork list of movie and cartoon of the horror genre
    """

    serializer_class = serializers.FilmWorkOtherSlidersSerializer

    def get_queryset(self):
        movies = models.FilmWork.objects.filter(type='movie', genres__name='ужасы')[:7]
        cartoons = models.FilmWork.objects.filter(type='cartoon', genres__name='ужасы')[:7]
        return movies | cartoons


class FilmWorkListMovieCartoonFamily(generics.ListAPIView):
    """
    FilmWork list of new movie and cartoon of the family genre
    """

    serializer_class = serializers.FilmWorkOtherSlidersSerializer

    def get_queryset(self):
        movies = models.FilmWork.objects.filter(type='movie', genres__name='семейный')[:7]
        cartoons = models.FilmWork.objects.filter(type='cartoon', genres__name='семейный')[:7]
        return movies | cartoons


class BrowsingHistoryCreateAPIView(generics.CreateAPIView):
    queryset = models.BrowsingHistory.objects.all()
    serializer_class = serializers.BrowsingHistorySerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile, film_work_id=self.request.kwargs['pk'])


class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = acc_serializer.ProfileSerializer


