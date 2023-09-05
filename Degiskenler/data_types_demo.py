'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    
    ** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)
'''
π=3.14
r=float(input("Dairenin Yarıçapını Gir : "))
daireAlan=π*(r**2)
daireCevre=2*π*r
print("Yarıçapı Girilen Dairenin Alanı : ",daireAlan)
print("Yarıçapı Girilen Dairenin Çevresi : ",daireCevre)

result="alan: "+str(daireAlan)+" çevre: "+str(daireCevre)
print(result)


'''
    Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
'''

meafeKm=int(input("Aracınızın KM 'sini giriniz : "))
mesafeMil=float(meafeKm)/1.609344
mesafeMil=round(mesafeMil,2) #mesafeMil değerinde virgülden sonra 2 karakter almamızı sağlamış olduk. Round fonksiyonu bu işe yarar.
print(str(meafeKm)+" km= "+str(mesafeMil)+" mil.")