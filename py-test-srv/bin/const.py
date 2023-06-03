URL = 'http://py-srv:5000'

GET_BY_COLOR_URL = URL + '/pop/color/clear'

GET_BY_BREED_URL = URL + '/pop/name/Verners'

GET_ALL_URL = URL + '/pop'

STATIC = {
  "results": {
    "count": 4,
    "data": [
      {
        "color": "brown",
        "id": 1,
        "name": "RC Cola"
      },
      {
        "color": "clear",
        "id": 2,
        "name": "Sprite"
      },
      {
        "color": "brown",
        "id": 3,
        "name": "Verners"
      },
      {
        "color": "green",
        "id": 4,
        "name": "Mt. Lightening"
      }
    ]
  }
}

INSERT_URL = URL + '/pop/name/Grape/color/purple'

SMOKE_URL = URL + '/'

SMOKE = {'results': {"hello": "world"}}
