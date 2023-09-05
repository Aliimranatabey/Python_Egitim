name='Ali İmran'
surname='Atabey'
age=22

print('My name is {} {}'.format(name,surname))
print('My name is {1} {0}'.format(name,surname))
print('My name is {s} {n}'.format(n=name,s=surname))
print("My name is {} {}. I'm {} years old.".format(name,surname,age))
print("My name is {0} {1}. I'm {2} years old.{2}".format(name,surname,age))

number=200/700
print('the result is {n:1.2}'.format(n=number))
print('the result is {n:10.4}'.format(n=number))

print(f"My name is {name}{surname} and I'm {age} years old.")