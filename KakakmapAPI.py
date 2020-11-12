import requests

Api_key = '#'
address = '경북 구미시 진평동 766'

url = 'https://dapi.kakao.com/v2/local/search/address'
head = {'Authorization':'KakaoAK '+Api_key}

params = {'query':address}
response = requests.get(url,headers=head,params=params).json()
document = response['documents'][0]
add = document['address']
latitude = add['y']
longitude = add['x']
print(address)
print(latitude,longitude)
