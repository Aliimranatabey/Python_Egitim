name='Ali İmran'
surname='Atabey'
age=22

print('My name is {} {}'.format(name,surname))                                  # My name is Ali İmran Atabey
print('My name is {1} {0}'.format(name,surname))                                # My name is Atabey Ali İmran
print('My name is {s} {n}'.format(n=name,s=surname))                            # My name is Atabey Ali İmran
print("My name is {} {}. I'm {} years old.".format(name,surname,age))           # My name is Ali İmran Atabey. I'm 22 years old. 
print("My name is {0} {1}. I'm {2} years old.{2}".format(name,surname,age))     # My name is Ali İmran Atabey. I'm 22 years old.22

number=200/700
print('the result is {n:1.2}'.format(n=number))                                 # the result is 0.29
print('the result is {n:10.4}'.format(n=number))                                # the result is     0.2857

print(f"My name is {name}{surname} and I'm {age} years old.")                   # My name is Ali İmranAtabey and I'm 22 years old.