from requests import get

file = open('images.txt', 'r+')
url = file.readlines()
file.close()

new_url_list = []
for e in url:
    new_url = e.rstrip('\n')
    new_url_list.append(new_url)

new_url_li = new_url_list[0]
r = get(new_url_li)
with open('pixa.jpg', 'wb') as file:
    file.write(r.content)

