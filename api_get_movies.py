import json

import requests

from app import models

received_data_json = requests.get('https://api.kinopoisk.dev/v1.3/'
                                  'movie?selectFields=name%20description%20premiere.world'
                                  '%20slogan%20year%20backdrop%20movieLength%20type%20budget'
                                  '%20poster%20genres%20videos.trailers%20persons'
                                  '%20ageRating&page=1&limit=3',
                                  headers={
                                      "X-API-KEY": "FA230QP-3HKM5E3-K4VVPF2-5516QR2"
                                  }
                                  )

received_data_python = json.loads(received_data_json.text)['docs']


for movie_dict in received_data_python:
    print(movie_dict)
    break
