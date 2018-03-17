def kciro(tsatismik,hmadde,bonarim,sgid,salınanhiz):
    kciro=tsatismik-(hmadde+bonarim+sgid+salınanhiz)
    return kciro
tsatismik=int(input("toplam satış miktarı"))
hmadde=int(input("hammadde"))
bonarim=int(input("bakım onarım giderleri"))
sgid=int(input("sevkiyat giderleri"))
salınanhiz=int(input("satın alınan hizmet giderleri"))
k=kciro(tsatismik,hmadde,bonarim,sgid,salınanhiz)
if(k>1000):
    print("işletme katma değer cirosu yüksek")
elif(500<k<999):
    print("işletme katma değer cirosu normal")
else:
    print("verimlilik kötü")




#müşterilerle çalışma süresi=çalışılan süre/toplam müşteri sayısı
#2016:çalışılan süre=170saat toplam müşteri sayısı=50
#2017:çalışılan süre=220saat toplam müşteri sayısı=70
#x=2016 yılı için çalışılan süre y=2016 yılı için toplam müşteri sayısı
#x=2017 yılı için çalışılan süre y=2017 yılı için toplam müşteri sayısı
def mustericalisma(x,y):
    global mustericalisma
    mustericalisma=x/y
    return mustericalisma
def mustericalisma2(x,y):
    global mustericalisma2
    mustericalisma2=(x+50)/(y+20)
    return mustericalisma2
def calismasurelerifarki(mustericalisma,mustericalisma2):
    calismasuref=mustericalisma-mustericalisma2
x=170
y=50
sure1=mustericalisma(x,y)
sure2=mustericalisma2(x,y)
calismasurelerifarki(sure1,sure2)




#ygelir:yazılım geliri
#fgelir:finansman geliri
#üsatisgel:ürün satış geliri
#cmaas:çalışan maaşları
#kgid:kira gideri
#dmal:donanım maliyeti
#yagelir:yazılım geliri
#sgelir:sponsorluk geliri
#egel:e ticaret geliri
#üsatgel:ürün satış geliri
#camaas:çalışan maaşları
#kigid:kira gideri
#bmal:bakım maliyeti
ygelir=int(input("yazılım gelirini giriniz."))
fgelir=int(input("finansman gelirini giriniz."))
üsatisgel=int(input("ürün satış gelirini giriniz."))
cmaas=int(input("çalışan maaşlarını giriniz."))
kgid=int(input("kira giderini giriniz."))
dmal=int(input("donanım maliytini giriniz."))
yagelir=int(input("yazılım gelirini giriniz."))
sgelir=int(input("sponsorluk gelirini giriniz."))
egel=int(input("e ticaret gelirini giriniz."))
üsatgel=int(input("ürün satış gelirini giriniz."))
camaas=int(input("çalışan maaşlarını giriniz."))
kigid=int(input("kira giderini giriniz."))
bmal=int(input("bakım maliyetini giriniz."))
                 
def ilkgelir(ygelir,fgelir,üsatisgel):
    global ilkgelir
    ilkgelir=ygelir+fgelir+üsatisgel
    return ilkgelir
def ilkgider(cmaas,kgid,dmal):
    global ilkgider
    ilkgider=cmaas+kgid+dmal
    return ilkgider
def songelir(yagelir,sgelir,egel,üsatgel):
    global songelir
    songelir=yagelir+sgelir+egel+üsatgel
    return songelir
def songider(camaas,kigid,bmal):
    global songider
    songider=camaas+kigid+bmal
    return songider
def işletmekarı(ilkgelir,ilkgider,songelir,songider):
    işletmekarı=(ilkgelir+songelir)-(ilkgider+songider)
    if(işletmekarı>5000):
        print("işletme çok karlı")
    elif(1000<işletmekarı<5000):
        print("işletme karı normal")
    else:
        print("işletme yeterince karda değil")
igelir=ilkgelir(ygelir,fgelir,üsatisgel)
igider=ilkgider(cmaas,kgid,dmal)
sgelir=songelir(yagelir,sgelir,egel,üsatgel)
sgider=songider(camaas,kigid,bmal)
işletmekarı(ilkgelir,ilkgider,songelir,songider)
     




