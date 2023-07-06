from django.shortcuts import render
from django.contrib.auth.models import User

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

class BaholashMezonViewSet(viewsets.ModelViewSet):
    queryset = BaholashMezon.objects.all()
    serializer_class = LoaderBaholashMezon
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class HududlarViewSet(viewsets.ModelViewSet):
    queryset = Hududlar.objects.all()
    serializer_class = LoaderHududlar
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
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


# @api_view(['get'])
# def Api_Tanlovlar(request):
#     tanovlar = []
#     url = "https://grant.mininnovation.uz/tour/index"
#     tanlovlar = get_data_tanlovlar(url)
#     get_all = requests.get(url)
#     html = BeautifulSoup(get_all.text,'html.parser')
#     pagination = html.find(class_="pagination")
#     for i in pagination.find_all(class_="page-item"):
#         for data in get_data_tanlovlar("https://grant.mininnovation.uz"+i.find("a")['href']):
#             tanlovlar.append(data)
    
#     DATA = {
#         "tanlovalar":tanlovlar,
#     }
#     return Response(DATA)


@api_view(['get'])
def Api_Tanlovlar(request):
    DATA = {
    "tanlovalar": [
        {
            "title": "Ilmiy faoliyatga oid davlat dasturlari doirasida “O’zbekiston-Belarus” fundamental loyihalar tanlovi e'lon qilinadi (79-tur)",
            "img": "https://assets-grant.mininnovation.uz/uploads/SZPt1NzX08mz9i1_jVjdXGoa-DGr7wbq.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=115",
            "sana": "01-may, 16:14",
            "mudat": "Muddat: 01-iyun, 22:00"
        },
        {
            "title": "Amaliy hamda innovatsion loyihalar tanlovining 77-turi e’lon qilinadi",
            "img": "https://assets-grant.mininnovation.uz/uploads/IJ-ktobBPPxe81YZP3HR05VVkEF55QwP.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=114",
            "sana": "28-mart, 15:34",
            "mudat": "Muddat: 01-may, 18:00"
        },
        {
            "title": "Innovatsion rivojlanish agentligi “Olima ayollar” tashabbuskor amaliy va innovatsion loyihalar tanlovi (78-tur) eʼlon qiladi",
            "img": "https://assets-grant.mininnovation.uz/uploads/xdejnL_nDCZZQd_phr-Menc-nj05NJqA.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=113",
            "sana": "06-may, 13:08",
            "mudat": "Muddat: 08-may, 18:00"
        },
        {
            "title": "“Ўзбекистон- Туркманистон” илмий лойиҳалар танлови",
            "img": "https://assets-grant.mininnovation.uz/uploads/yj-PWjw4waoDt7DAlfT__MZ3xKT00UiN.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=112",
            "sana": "13-yanvar, 10:05",
            "mudat": "Muddat: 31-mart, 18:00"
        },
        {
            "title": "Илмий фаолиятга оид давлат дастурлари доирасида бажариладиган амалий ва инновацион лойиҳалар танловининг 18-72-турлари қуйидаги фан йўналишлари бўйича қайта эълон қилинади",
            "img": "https://assets-grant.mininnovation.uz/uploads/IdmnusyoZpyxNcgwSyYVycemqEE4nSas.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=111",
            "sana": "19-noyabr, 16:01",
            "mudat": "Muddat: 19-dekabr, 18:00"
        },
        {
            "title": "Amaliy va innovatsion loyihalar tanlovining 74-turi e'lon qilinadi",
            "img": "https://assets-grant.mininnovation.uz/uploads/sHPzrDZJ6KTdr4uGKvhL_JW7tLMXUJm8.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=110",
            "sana": "14-noyabr, 17:17",
            "mudat": "Muddat: 01-dekabr, 18:00"
        },
        {
            "title": "Ilmiy faoliyatga oid davlat dasturlari doirasida “O’zbekiston-Belarus” fundamental loyihalar tanlovi e'lon qilinadi (79-tur)",
            "img": "https://assets-grant.mininnovation.uz/uploads/SZPt1NzX08mz9i1_jVjdXGoa-DGr7wbq.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=115",
            "sana": "01-may, 16:14",
            "mudat": "Muddat: 01-iyun, 22:00"
        },
        {
            "title": "Amaliy hamda innovatsion loyihalar tanlovining 77-turi e’lon qilinadi",
            "img": "https://assets-grant.mininnovation.uz/uploads/IJ-ktobBPPxe81YZP3HR05VVkEF55QwP.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=114",
            "sana": "28-mart, 15:34",
            "mudat": "Muddat: 01-may, 18:00"
        },
        {
            "title": "Innovatsion rivojlanish agentligi “Olima ayollar” tashabbuskor amaliy va innovatsion loyihalar tanlovi (78-tur) eʼlon qiladi",
            "img": "https://assets-grant.mininnovation.uz/uploads/xdejnL_nDCZZQd_phr-Menc-nj05NJqA.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=113",
            "sana": "06-may, 13:08",
            "mudat": "Muddat: 08-may, 18:00"
        },
        {
            "title": "“Ўзбекистон- Туркманистон” илмий лойиҳалар танлови",
            "img": "https://assets-grant.mininnovation.uz/uploads/yj-PWjw4waoDt7DAlfT__MZ3xKT00UiN.jpg",
            "link": "https://grant.mininnovation.uz//tour/view?id=112",
            "sana": "13-yanvar, 10:05",
            "mudat": "Muddat: 31-mart, 18:00"
        },
    ]
}
    return Response(DATA)


def get_data_news(url):
    tanovlar = []
    url = url
    get_all = requests.get(url)
    html = BeautifulSoup(get_all.text,'html.parser')
    cards = html.find('table')
    # print(cards)
    for i in cards.find_all("td"):
        img = i.find("img")
        if img == None:
            continue

        img = img['src']
        print(img)
        # link = "https://grant.mininnovation.uz/"+i.find("a")['href']
        date = i.find_all("span")[-1].get_text()
        manba = i.find("span").find("a")
        manba_nomi = manba.get_text()
        manba = manba['href']
        title = i.find("a")
        link = "https://edu.uz/"+title['href']
        title=title.get_text()
        text=i.find('p',class_='blog_text')
        text=text.find_next_sibling('p')
        print(text)
        if text == None:
            pass
        else:
            text=text.get_text()
        tanovlar.append(
            {"title":title,"text":text,"link":link,"img":img,"sana":date,"manba_link":manba,"manba_nomi":manba_nomi}
        )
    return tanovlar

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = LoaderNew
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]
    
    # def list(self, request):
    #     queryset = New.objects.all()
    #     serializer = LoaderNew(queryset, many=True)
        
    #     eduuz = get_data_news("https://edu.uz/uz/news/index")

    #     DATA = {
    #         "edu.uz":eduuz,
    #         "local":serializer.data
    #     }
    #     return Response(DATA)
    def list(self, request):
        queryset = New.objects.all()
        serializer = LoaderNew(queryset, many=True)
        eduuz = [
        {
            "title": "Xitoy Fanlar akademiyasi rahbariyati va professor-olimlarining Orolboʻyiga rasmiy tashrifi boʻldi",
            "text": "Oʻzbekiston Respublikasi Prezidenti huzuridagi Orolboʻyi xalqaro innovatsiya markazi va Xitoy Fanlar akademiyasi Sinszyan ekologiya va geografiya instituti (XIEG) bir necha yillardan buyon hamkorlik qilib, qoʻshma ekologik yoʻnalishdagi loyihalarni amalga oshirib kelmoqda.",
            "link": "https://edu.uz//uz/news/view/5334",
            "img": "https://edu.uz/media/b2955538-2903-411e-b9cb-37072faf3892.jpg",
            "sana": "10.05.2023",
            "manba_link": "http://edu.uz/uz/pages/axb",
            "manba_nomi": "Axborot xizmati"
        },
        {
            "title": "Qurilish materiallari sanoati sohasiga ilm-fan yutuqlari va innovatsion texnologiyalar keng joriy etilmoqda",
            "text": "10-may kuni Oʻzbekiston Respublikasi Oliy taʼlim, fan va innovatsiyalar vazirligi, Oʻzbekiston Respublikasi Fanlar akademiyasi, “Oʻzsanoatqurilishmateriallari“ uyushmasi hamkorligida “2022 yilda Qurilish materiallari sohasida ilm-fan yutuqlari, innovatsion g‘oyalar boʻyicha amalga oshirilgan ishlar tahlili” mavzusida matbuot anjumani oʻtkazildi. Unda sohadagi yangilik va oʻzgarishlar, amalga oshirilgan kashfiyot va ilmiy ishlar, ilg‘or innovatsion g‘oyalar haqida maʼlumotlar berildi.",
            "link": "https://edu.uz//uz/news/view/5335",
            "img": "https://edu.uz/media/1a3e604c-1af6-efe9-0b72-196e5d9c128a.jpg",
            "sana": "10.05.2023",
            "manba_link": "http://edu.uz/uz/pages/axb",
            "manba_nomi": "Axborot xizmati"
        },
        {
            "title": "Qachonki, tadqiqotchining ilmiy faoliyatini ilmiy hamjamiyat tan olsagina, u olimga aylanadi – vazir",
            "text": "Oliy ta’lim, fan va innovatsiyalar vaziri, akademik Ibrohim Abdurahmonov Toshkent shahridagi Turin politexnika universitetida bo‘lib, talabalar uchun yaratilgan sharoitlarni ko‘zdan kechirdi. Professor-o‘qituvchilar hamda talabalar bilan uchrashib, ular faoliyatidagi muammo va takliflari yuzasidan samimiy suhbat o‘tkazdi.",
            "link": "https://edu.uz//uz/news/view/5336",
            "img": "https://edu.uz/media/f26435f1-c5fb-33a6-f7e2-7eeeae90497f.jpg",
            "sana": "10.05.2023",
            "manba_link": "http://edu.uz/uz/pages/axb",
            "manba_nomi": "Axborot xizmati"
        },
        {
            "title": "Vazir fuqarolar murojaatlari bo‘yicha navbatdagi qabulni o‘tkazdi",
            "text": "",
            "link": "https://edu.uz//uz/news/view/5333",
            "img": "https://edu.uz/media/2fff5637-061e-82b1-5a64-b853d1086669.JPG",
            "sana": "06.05.2023",
            "manba_link": "http://edu.uz/uz/pages/axb",
            "manba_nomi": "Axborot xizmati"
        },
        {
            "title": "Xalqaro hamkorlik",
            "text": "Oliy taʼlim, fan va innovatsiyalar vazirligi va Germaniya xalqaro hamkorlik jamiyati (GIZ)ning O‘zbekistondagi vakolatxonasi mutaxassislari hamkorligida 4-5-may kunlari Qoraqalpog‘iston Respublikasida professional taʼlim muassasalari oʼquvchilari uchun “Hududiy mehnat yarmarkasi va ijtimoiy sherikchilik mintaqaviy forumi” tashkil etildi.",
            "link": "https://edu.uz//uz/news/view/5330",
            "img": "https://edu.uz/media/691bf905-61fd-ab54-6bc0-a2bcdea6e0f5.jpg",
            "sana": "05.05.2023",
            "manba_link": "http://edu.uz/uz/pages/axb",
            "manba_nomi": "Axborot xizmati"
        },
        {
            "title": "Vazir yangi tayinlangan professional ta’lim muassasalari direktorlari bilan uchrashdi",
            "text": "",
            "link": "https://edu.uz//uz/news/view/5332",
            "img": "https://edu.uz/media/4ff1dcef-2388-5443-2557-f6e1b0619fe9.jpg",
            "sana": "05.05.2023",
            "manba_link": "http://edu.uz/uz/pages/axb",
            "manba_nomi": "Axborot xizmati"
        },
        {
            "title": "“O‘zbekiston professional ta’lim tizimida sifatni ta’minlash va kasbiy ko‘nikmalarni rivojlantirish” mavzusida xalqaro konferensiyasi",
            "text": "O‘zbekiston Respublikasi Prezidentining 2023-yil 28-fevraldagi PF-27-son Farmoni bilan tasdiqlangan 2022 – 2026-yillarga mo‘ljallangan Yangi O‘zbekistonning taraqqiyot strategiyasini “Insonga e’tibor va sifatli ta’lim yili”da amalga oshirishga oid Davlat dasturining 150-bandida “Yevropa kasbiy ta’lim va kasbga o‘qitish sifatini ta’minlash (EQAVET) tizimi talablariga to‘liq javob beradigan namunaviy professional ta’lim muassasalari faoliyatini yo‘lga qo‘yish” vazifasi belgilangan.",
            "link": "https://edu.uz//uz/news/view/5327",
            "img": "https://edu.uz/media/e5d9131b-004e-f357-2867-c3ae272d37c2.jpg",
            "sana": "04.05.2023",
            "manba_link": "http://edu.uz/uz/pages/axb",
            "manba_nomi": "Axborot xizmati"
        }
    ]

        DATA = {
            "edu.uz":eduuz,
            "local":serializer.data
        }
        return Response(DATA)
    
@api_view(['post'])
def Api_Login(request):
    print(request.data)
    username = request.data['username']
    password = request.data['password']
    try:
        user=User.objects.get(username=username)
        if user.check_password(password):
            try:
                token=Token.objects.get(user=user)
            except:
                token=Token.objects.create(user=user)
            return Response({"status":True,"token":token.key})
        else:
            return Response({"status":False},status=400)
    except Exception as r:
        print(r)
        return Response({"status":False},status=400)
