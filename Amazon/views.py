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
        # //////////////////////////////////

        url = 'https://www.flipkart.com/search?q='
        query = request.POST.get('searchbox')
        query = query.replace(' ','+')
        url+=query
        page = requests.get(url)
        soup = BeautifulSoup(page.content)

        fname = None #name
        if(soup.find(class_='_4rR01T')==None):
            fname = soup.find(class_='s1Q9rs')
        else:
            fname = soup.find(class_='_4rR01T')
        fprice = soup.find(class_='_30jeq3') #price
        
        freviews = soup.find(class_='_3LWZlK') #review points
        frev = soup.select('span._2_R_DZ')
        frev2 = frev[0].find_all('span')
        fpeople_rated = frev2[1].text
        fpeople_reviewed = frev2[3].text


        # ////////////////////////////////////////////
        url = 'https://www.snapdeal.com/search?keyword='
        query = request.POST.get('searchbox')
        query = query.replace(' ','+')
        url+=query
        page = requests.get(url)
        soup = BeautifulSoup(page.content)
       
        sname = soup.find(class_='product-title') #name
        sprice = soup.find(class_='lfloat product-price') #price
        sreviews = soup.find(class_='product-rating-count')

        
    context = {
        'price' : price,
        'name' : name,
        'reviews' : reviews,
        'peopleRated' : peopleRated,
        'image' : image,

        'fname':fname.text,
        'fprice':fprice.text,
        'freviews':freviews.text,
        'fpeople_rated':fpeople_rated,
        'fpeople_reviewed':fpeople_reviewed,

        'sname':sname.text,
        'sprice':sprice.text,
        'sreviews':sreviews.text,

    }
    return render(request, 'product.html', context)
