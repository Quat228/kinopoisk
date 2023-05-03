import json

import requests

from app import models

received_data_json = requests.get('https://api.kinopoisk.dev/v1.3/movie?selectFields=backdrop%20movieLength'
                                  '%20type%20name%20description%20premiere.world%20slogan%20year%20budget'
                                  '%20poster%20genres%20videos.trailers%20persons'
                                  '%20ageRating&page=1&limit=1&type=movie&typeNumber=1&year=1990-2030&poster.url='
                                  '%21null&backdrop.url=%21null&videos.trailers.site=youtube',
                                  headers={
                                      "X-API-KEY": "3JE8DNH-8VX416N-KWCW970-FE19HE4"
                                  }
                                  )

received_data_python = json.loads(received_data_json.text)['docs']

exist_movies = []

skipped_movies = []


skipped = 0

approved = 0


def get_query_names(model_name):
    list1 = []
    for dict_name in model_name.objects.values('name'):  # <QuerySet [{'name': '1+1'}, {'name': '1+1'}]>
        list1.append(dict_name['name'])
    return list1


def create_and_get_object(model_name, value):
    if value in get_query_names(model_name):
        obj = model_name.objects.filter(name=value).first()  # c1 - экземпляр
    else:
        obj = model_name.objects.create(name=value)  # c1 - экземпляр
    return obj


for movie_dict in received_data_python:
    # -- Система проверки на наличие фильма в базе данных
    if movie_dict['name'] in get_query_names(models.FilmWork):
        exist_movies.append(f"{movie_dict['name']}")
        print(f"Movie {movie_dict['name']} is already exist")
        continue
    # -- Добавление фильма в бд
    c1 = None
    list_genre_objects = []
    list_person_objects = []
    try:
        # - Добавления валюты
        currency = create_and_get_object(models.Currency, movie_dict['budget']['currency'])
        # - Добавление жанра
        for genre_dict in movie_dict['genres']:
            genre = create_and_get_object(models.Genre, genre_dict['name'])
            list_genre_objects.append(genre)
        # - Добавление актерского состава
        for person_dict in movie_dict['persons']:
            if person_dict['name'] and person_dict['photo'] and person_dict['name']:
                if person_dict['name'] in get_query_names(models.Person):
                    person = models.Person.objects.filter(name=person_dict['name']).first()
                else:
                    person = models.Person.objects.create(
                        name=person_dict['name'],
                        photo=person_dict['photo'],
                        profession=person_dict['profession']
                    )
                list_person_objects.append(person)
        # - Добавление фильма
        movie1 = models.FilmWork.objects.create(
            backdrop=movie_dict['backdrop']['url'],
            movie_length=movie_dict['movieLength'],
            type=movie_dict['type'],
            name=movie_dict['name'],
            description=movie_dict['description'],
            premiere=movie_dict['premiere']['world'],
            slogan=movie_dict['slogan'],
            year=movie_dict['year'],
            budget=movie_dict['budget']['value'],
            currency=c1,
            poster=movie_dict['poster']['url'],
            trailer_url=movie_dict['videos']['trailers'][0]['url'],
            age_rating=movie_dict['ageRating']
        )
        movie1.genres.set(list_genre_objects)
        movie1.persons.set(list_person_objects)
        print(f"Filmwork {movie_dict['name']} has just downloaded")
        approved += 1
    except Exception as e:
        skipped_movies.append(movie_dict['name'])
        print(f"Skipped filmwork {movie_dict['name']} - reason: {e}")
        skipped += 1


print(exist_movies)
print(skipped_movies)

print(f"Approved {approved}")
print(f"Skipped {skipped}")
print(f"Exist {len(exist_movies)}")

