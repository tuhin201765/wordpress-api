from requests import get
from pprint import pprint
query = 'yellow+flowers'
api_key ='32029211-b9a80ab832d0119c08a0b3979'
url = f'https://pixabay.com/api/?key={api_key}&q={query}&image_type=photo&pretty=true'
r = get(url)
api_data = r.json().get('hits')
pprint(api_data)
# res = api_data[0]
# pprint(res)
for data in api_data:
    webformatURL = data.get('webformatURL')
    largeImageURL = data.get('largeImageURL')
    file = open('images.txt', 'a+')
    file.writelines(webformatURL + '\n')
    file.close()
    # print(image_url)