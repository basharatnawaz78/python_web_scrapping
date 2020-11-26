from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup


# Create your views here.
def index(request):
    return render(request, 'index.html')

def product(request):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    print("hello")
    if request.method == "POST":
        searchItem = request.POST.get('searchbox')
        searchItem = searchItem.replace(' ','+')
        url = 'https://www.amazon.in/s?k=' + searchItem + '&rh=n%3A1389401031&ref=nb_sb_noss'
        r = requests.get(url,headers=headers)
        content = r.content
        soup = BeautifulSoup(content,'html.parser')

        image = soup.find(class_='a-section aok-relative s-image-fixed-height')
        image = image.find('img')
        image = image['src']

        name = soup.find(class_='a-size-medium a-color-base a-text-normal').text #name
        price = soup.find(class_='a-price-whole').text #price
        reviews = soup.find(class_='a-icon a-icon-star-small a-star-small-4 aok-align-bottom').text #review points
        people = soup.find(class_='a-row a-size-small') #people
        peopleRated = people.find(class_='a-size-base').text #peopleRated
        
       
        
    context = {
        'price' : price,
        'name' : name,
        'reviews' : reviews,
        'peopleRated' : peopleRated,
        'image' : image

    }
    return render(request, 'product.html', context)
