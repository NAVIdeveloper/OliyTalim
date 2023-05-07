from django.shortcuts import render
from .models import *
from .serializers import *
import requests
from bs4 import BeautifulSoup
# Create your views here.
# from django.db.models import Max,Min,Q as SearchQ

from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes,action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from django.contrib.auth import authenticate


class RahbarlarViewSet(viewsets.ModelViewSet):
    queryset = Rahbarlar.objects.all()
    serializer_class = LoaderRahbarlar
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class IshlarViewSet(viewsets.ModelViewSet):
    queryset = Ishlar.objects.all()
    serializer_class = LoaderIshlar
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class ArizaViewSet(viewsets.ModelViewSet):
    queryset = Ariza.objects.all()
    serializer_class = LoaderAriza
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "create" or self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

def get_data_tanlovlar(url):
    tanovlar = []
    url = url
    get_all = requests.get(url)
    html = BeautifulSoup(get_all.text,'html.parser')
    cards = html.find(class_="trends__content cards")
    for i in cards.find_all(class_="col-sm-6 col-xl-4"):
        img = i.find("img")['src']
        link = "https://grant.mininnovation.uz/"+i.find("a")['href']
        date = i.find("p").get_text()
        title = i.find(class_="text__three-line").get_text()
        mudat = i.find(class_="card__footer-bottom").find("a").get_text().split()
        tanovlar.append(
            {'title':title,"img":img,"link":link,"sana":date,"mudat":" ".join(mudat)}
        )
    return tanovlar


@api_view(['get'])
def Api_Tanlovlar(request):
    tanovlar = []
    url = "https://grant.mininnovation.uz/tour/index"
    tanlovlar = get_data_tanlovlar(url)
    get_all = requests.get(url)
    html = BeautifulSoup(get_all.text,'html.parser')
    pagination = html.find(class_="pagination")
    for i in pagination.find_all(class_="page-item"):
        for data in get_data_tanlovlar("https://grant.mininnovation.uz"+i.find("a")['href']):
            tanlovlar.append(data)
    
    DATA = {
        "tanlovalar":tanlovlar,
    }
    return Response(DATA)

# @api_view(['get'])
# def Api_Tanlov(request):
#     url = request.GET['url']
#     get_all = requests.get(url)
#     html = BeautifulSoup(get_all.text,'html.parser')
    
#     DATA = {
    
#     }
#     return Response(DATA)
