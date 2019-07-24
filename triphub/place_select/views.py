from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.

def place_select(request):
    return render(request , 'place_select.html')


def attraction(request):
    attraction_get = []
    if request.method == 'GET':
        pick = request.GET['select_place']
        
                
        req = requests.get('https://m.search.naver.com/search.naver?where=m&query=%EC%A0%84%EA%B5%AD+%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&x_trv=Ml8wMF8wXw%3D%3D&sm=mtb_trv')
        html = req.text
        soup = bs(html, 'html.parser')

        divs = soup.findAll('div' , {"class" : "map_marker"})
        

        for div in divs:
            
            links = div.find_all('a', {'href':True})
            
            for link in links:
                linkname = link.findAll('span' , {'class' : 'spot'})
        
                for yo in linkname:
                    name_only = yo.text
            
                    if name_only == pick:
                    
                        req2 = requests.get("https://m.search.naver.com"+link['href'])
                        html2 = req2.text

                        soup2 =bs (html2,'html.parser')

                        attractions = soup2.findAll('div' , {'class' : 'info'})
                        
                        for attraction in attractions:
                            at = attraction.find_all('strong' ,{'class' : 'tit'})
                            
                            
                            for hi in at:
                                hello = hi.text
                                attraction_get.append(hello)
                                
                        

    return render(request , 'place_select.html' , {'attraction' : attraction_get})




def next_select_page(request):
    if request.method == 'GET':
        pick = request.GET['select_place']
        
        return render(request , 'next_select/' + pick + '.html')

