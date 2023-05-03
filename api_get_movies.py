import json

import requests

from app import models

received_data_json = requests.get('https://api.kinopoisk.dev/v1.3/'
                                  'movie?selectFields=name%20description%20premiere.world'
                                  '%20slogan%20year%20backdrop%20movieLength%20type%20budget'
                                  '%20poster%20genres%20videos.trailers%20persons'
                                  '%20ageRating&page=1&limit=2',
                                  headers={
                                      "X-API-KEY": "FA230QP-3HKM5E3-K4VVPF2-5516QR2"
                                  }
                                  )

received_data_python = json.loads(received_data_json.text)['docs']

exist_movies = []


def get_query_names(model_name, ):
    list1 = []
    for dict_name in model_name.objects.values('name'):  # <QuerySet [{'name': '1+1'}, {'name': '1+1'}]>
        list1.append(dict_name['name'])
    return list1


for movie_dict in received_data_python:
    # -- Система проверки на наличие фильма в базе данных
    if movie_dict['name'] in get_query_names(models.Movie):
        exist_movies.append(f"{movie_dict['name']}")
        continue
    # -- Добавление фильма в бд
    # - Добавления валюты
    if movie_dict['budget']['currency'] in get_query_names(models.Currency):
        c1 = models.Currency.objects.filter(name=movie_dict['budget']['currency']).first()  # c1 - экземпляр
    else:
        c1 = models.Currency.objects.create(name=movie_dict['budget']['currency'])  # c1 - экземпляр
    # - Добавление жанра
    list_genre_objects = []
    for genre_dict in movie_dict['genres']:
        if genre_dict['name'] in get_query_names(models.Genre):
            genre = models.Genre.objects.filter(name=genre_dict['name']).first()
        else:
            genre = models.Genre.objects.create(name=genre_dict['name'])
        list_genre_objects.append(genre)




print(exist_movies)





























