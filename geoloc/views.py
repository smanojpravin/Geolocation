from django.shortcuts import render
import requests


def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR','')
    response = requests.get('http://api.ipstack.com/%s?access_key=d695eb1c16c74da8ddfdd76f2f77381e'%ip_address)
    print(response)
    geodata = response.json()
    print(geodata)
    
    return render(request,'geoloc/home.html',{
        'ip':geodata['ip'],
        'country': geodata['region_name'],
        'latitude':geodata['latitude'],'longitude':geodata['longitude'],'api_key':'AIzaSyCRCW80dmZKVTuLldsEFzgd5Te1Y9Jum8s' 
        })