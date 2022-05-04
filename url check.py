import urllib.request
get_url=urllib.request.urlopen('https://www.google.com/maps')
print("response status: "+ str(get_url.getcode()))


