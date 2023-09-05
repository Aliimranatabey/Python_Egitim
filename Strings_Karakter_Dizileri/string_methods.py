msg="Python kursumuza Hoş geldiniz. Ben Ali imran Atabey."

print(msg.upper())                  # PYTHON KURSUMUZA HOŞ GELDINIZ. BEN ALI IMRAN ATABEY.
print(msg.lower())                  # python kursumuza hoş geldiniz. ben ali imran atabey.
print(msg.title())                  # Python Kursumuza Hoş Geldiniz. Ben Ali Imran Atabey.
print(msg.capitalize())             # Python kursumuza hoş geldiniz. ben ali imran atabey.

print("abc".islower())              # True

print("      abc ".strip())         # abc
print(msg.split())                  # ['Python', 'kursumuza', 'Hoş', 'geldiniz.', 'Ben', 'Ali', 'imran', 'Atabey.']
print(msg.split('.'))               # ['Python kursumuza Hoş geldiniz', ' Ben Ali imran Atabey', '']

print("-".join(msg.split('.')))     # Python kursumuza Hoş geldiniz- Ben Ali imran Atabey-

print(msg.index('Hoş'))             # 17

print(msg.startswith('A'))          # False
print(msg.endswith('n'))            # False

print(msg.replace("Ali","Yunus"))   # Python kursumuza Hoş geldiniz. Ben Yunus imran Atabey.
print(msg.lower().replace(' ','-').replace('ş','s').replace('.','').replace('ı','i')) # python-kursumuza-hos-geldiniz-ben-ali-imran-atabey
