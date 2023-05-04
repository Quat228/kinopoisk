from rest_framework import generics
from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from . import models
from . import serializers


class FilmWorkListCreateAPIView(generics.ListAPIView):
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


class FilmWorkRetrieveUpdateDestroyAPIView(views.APIView):
    """
    FilmWork Retrieve, Update and Destroy View
    """
    def get_object(self, pk):
        return get_object_or_404(models.FilmWork, pk=pk)

    def get(self, request, pk, *args, **kwargs):
        serializer = serializers.FilmWorkSerializer(instance=self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        serializer = serializers.FilmWorkSerializer(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        self.get_object(pk).delete()
        return Response(status=204)
