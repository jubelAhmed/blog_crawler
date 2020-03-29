import requests

from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus

from . import models

# Create your views here

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={0}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def index(request):

    if request.method == 'POST':
        search = request.POST.get('search-item')
        finalurl = BASE_CRAIGSLIST_URL.format(quote_plus(str(search)))
        models.Search.objects.create(search=search)
        response = requests.get(finalurl)
        data = response.text
        soup = BeautifulSoup(data)

        post_listings = soup.find_all('li',{'class':'result-row'})
        final_posting = []
        for post in post_listings:
            post_title = post.find(class_='result-title').text
            post_url = post.find('a').get('href')
            if post.find(class_='result-price'):
                post_price = post.find(class_='result-price').text
            else:
                post_price = 'N/A'

            if post.find(class_='result-image').get('data-ids'):
                post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
                post_image_url = BASE_IMAGE_URL.format(post_image_id)
            else:
                post_image_url = 'N/A'

            final_posting.append((post_title, post_url, post_price,post_image_url))

        # post_title1 = soup.find_all('a',{'class':'result-title'})
        # print(post_title1[0].get('href '))
    elif request.method == 'GET':
        search = ''
        final_posting = []
    front_end_stuff = {
        'search':search,
        'final_posting':final_posting
    }
    return render(request, 'test_app/index.html',context=front_end_stuff)

