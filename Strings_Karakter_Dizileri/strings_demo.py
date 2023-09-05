website="http://www.sadikturan.com"
kursAdi="Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
karakterSayisi=len(kursAdi)
print("'kursAdi' karakter dizisinde {} karakter vardır.".format(karakterSayisi))

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])

# 3- 'website' içinden com karakterlerini alın.
print(website[karakterSayisi-3:karakterSayisi])

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
print("İlk 15 : "+kursAdi[0:15])
print("Son 15 : "+kursAdi[-15:])

# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
print(kursAdi[::-1])

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s="Hello world"
s=s[0:6]+'W'+s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
print('abc'*3)

name,surname,age,job='Sadık','Turan',37,'eğitimci'
# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Sadık Turan, Yaşım 37 ve mesleğim öğretmen.' 
print("Benim adım {} {}, Yaşım {} ve mesleğim {}".format(name,surname,age,job))
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")
