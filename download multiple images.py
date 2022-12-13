from requests import get
with open('images.txt', 'r') as file:
    url_list = file.readlines()
i=0
for url in url_list:
    r= url.rstrip('\n')
    res = get(r)
    with open (f'images/{i}.jpg','wb') as file:
        file.write(res.content)
    i+=1