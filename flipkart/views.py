from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import requests
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    context = {
        "data" : 205119002,
        "section" : "even"
    }
    return render(request,'index.html',context)

def submit(request):
    url = 'https://www.flipkart.com/search?q='
    query = request.POST.get('pname')
    query = query.replace(' ','+')
    url+=query
    page = requests.get(url)
    soup = BeautifulSoup(page.content)

    name = None #name
    if(soup.find(class_='_4rR01T')==None):
        name = soup.find(class_='s1Q9rs')
    else:
        name = soup.find(class_='_4rR01T')
    price = soup.find(class_='_30jeq3') #price
    
    reviews = soup.find(class_='_3LWZlK') #review points
    rev = soup.select('span._2_R_DZ')
    rev2 = rev[0].find_all('span')
    people_rated = rev2[1].text
    people_reviewed = rev2[3].text


    context = {
        'name':name.text,
        'price':price.text,
        'reviews':reviews.text,
        'people_rated':people_rated,
        'people_reviewed':people_reviewed,
    }
    print(url)
    return render(request,'submit.html',context)
