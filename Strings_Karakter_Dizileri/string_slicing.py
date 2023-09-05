ad = 'Ali İmran'
soyad = 'Atabey'
yas = '22'

msj = 'Benim adım ' + ad + ' ve soyadım ' + soyad + '.Yaşım ise ' + yas + '.'
karakterSayisi = len(msj)

print(msj[0])                   # B
print(msj[1])                   # e
print(msj[-1])                  # .
print(msj[karakterSayisi - 1])  # .

print(msj[0:5])                 # Benim
print(msj[6:16])                # adım Ali İ
print(msj[:10])                 # Benim adım
print(msj[10:])                 #  Ali İmran ve soyadım Atabey.Yaşım ise 22.

print(msj[-10:-1])              # ım ise 22
print(msj[0:40:2])              # Bnmaı l ma esydmAae.
print(msj[::1])                 # Benim adım Ali İmran ve soyadım Atabey.Yaşım ise 22.
print(msj[::-1])                # .22 esi mışaY.yebatA mıdayos ev narmİ ilA mıda mineB
