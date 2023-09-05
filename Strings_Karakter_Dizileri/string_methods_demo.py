website="http://www.sadikturan.com"
kursAdi="Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
print(" Hello World ".strip())
sonuc=' Hello World '.lstrip()
sonuc=' Hello World '.rstrip()
sonuc=website.lstrip('/:pthw.') # website içerisindeki soldan silinmesini istediğimiz değerlerin her birinden bir tane yazmamız yeterli olacaktır .
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
print("www.sadikturan.com".strip('w.moc'))
# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
print(kursAdi.lower())
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
print("Website url içerisinde Kac tane a karakteri var ? ",website.count('a'))
sonuc=website.count('www',0,10) #0 dan 10. indexe kadar www var mı diye kontrol eder .
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
print("www ile başlıyor mu ? ",website.startswith('www'))
print("com ile başlıyor mu ? ",website.endswith('com'))
# 6- 'website' içinde '.com' ifadesi var mı?
print(website.find('.com'))
sonuc=website.find('com',0,10)
sonuc=kursAdi.find('Python')
sonuc=kursAdi.rfind('Python')

sonuc=kursAdi.index('Python') # find da bulamazsa -1 dönderir ancak index de bulamazsa sistem hata verir
sonuc=kursAdi.rindex('Python')
# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print("kursAdi karakterleri alfabetik mi ? ",kursAdi.isalpha())
print("kursAdi karakterlerinde digital değer var mı ? ",kursAdi.isdigit())
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
msg="Contents"
print(msg.center(50,'*'))
sonuc=msg.ljust(50,'*')
sonuc=msg.rjust(50,'*')
# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
print(kursAdi.replace(' ','-'))
# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print('Hello World'.replace('World','There'))
# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
kursAdi=kursAdi.lower().replace(':','')
print(kursAdi.split(" "))