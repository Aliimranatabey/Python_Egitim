"""
    Uygulama 1: Bir öğrencinin aşağıdaki bilgileri için gerekli değişkenleri oluşturunuz.
    Öğrenci adı
    Öğrenci soyadı
    Öğrenci ad + soyad
    Öğrenci numarası
    Öğrenci cinsiyet
    Öğrenci tc kimlik
    Öğrenci doğum yılı
    Öğrenci adres bilgisi   
    Öğrenci yaşı 
"""
studentName="Ali İmran"
studentSurname="Atabey"
student=studentName+' '+studentSurname
print(student)
studentNumber="190541004"
studentGender=True #Erkek
print(studentGender)
studentGender=False #Kadın
print(studentGender)
studentTcNumber="28055555555"
studentBirthYear=2001
studentAddress="Pendik/İstanbul"
print(studentAddress)
studentAge=2023-studentBirthYear
print(studentAge)

"""
    Uygulama 2: Aşağıdaki ürünlerin toplam bilgisini hesaplayınız.
    
    Ürün 1 => 50     TL
    Ürün 2 => 60.5   TL
    Ürün 3 => 356.45 TL
"""

urun1=50
urun2=60.5
urun3=356.45

total=urun1+urun2+urun3
print("Toplam : ",total)