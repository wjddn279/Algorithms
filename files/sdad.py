import requests
import pandas as pd
import os
from ast import literal_eval

for dirname, _, filenames in os.walk('./DDD'):
    for filename in filenames:
        print(filename)
        url = os.path.join(dirname, filename)
        data = pd.read_csv(url)

data = data.drop(['poster_path'],axis=1)
data = data.drop(['Unnamed: 0'],axis=1)
print(data.columns)
data['poster_path']=0
print(data.columns)
length = len(data['id'])

for i in range(length):
    crews = literal_eval(str(data['crew'][i]))
    crews = crews[0:1]
    for j in range(len(crews)):
        crew  = literal_eval(str(crews[j]))
        url = 'https://api.themoviedb.org/3/person/' + str(crew['id']) + '?api_key=66c1f47425224432e41944275e7028c5'
        response = requests.get(url)
        json1 = response.json()
        var = json1.get('profile_path',0)
        if var == 0:
            crew['profile_path'] = '/dykOcAqI01Fci5cKQW3bEUrPWwU.jpg'
        else:
            crew['profile_path'] = json1['profile_path']
    data['crew'][i] = str(crews)
    if i%100 == 0:
        print(i)
        print(data['crew'][i])

for i in range(length):
    casts = literal_eval(str(data['cast'][i]))
    casts = casts[0:4]
    for j in range(len(casts)):
        cast  = literal_eval(str(casts[j]))
        url = 'https://api.themoviedb.org/3/person/' + str(cast['id']) + '?api_key=66c1f47425224432e41944275e7028c5'
        response = requests.get(url)
        json1 = response.json()
        var = json1.get('profile_path',0)
        if var == 0:
            cast['profile_path'] = '/dykOcAqI01Fci5cKQW3bEUrPWwU.jpg'
        else:
            cast['profile_path'] = json1['profile_path']
    data['cast'][i] = str(casts)
    if i%100 == 0:
        print(i)
        print(data['cast'][i])

for i in range(length):
    url = 'https://api.themoviedb.org/3/movie/' + str(data['id'][i]) + '?api_key=66c1f47425224432e41944275e7028c5'
    response = requests.get(url)
    json1 = response.json()
    var = json1.get('poster_path',0)
    if  var==0:
        data['poster_path'][i]='/dykOcAqI01Fci5cKQW3bEUrPWwU.jpg'
    else:
        data['poster_path'][i] = json1['poster_path']
    if not i%100:
        print(i)
        print(data['title'][i])
        print(data['poster_path'][i])

data.to_csv("./final.csv",mode="w",index='false')
