#1.Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
Name=input('Enter your name:')
Birthday=int(input('Enter your birthday:'))
from datetime import datetime
year=datetime.now().year
age=year-Birthday
print(f'My name is {Name}, I am {Birthday} years old')


#2.Extract car names from the following text:
txt = 'LMaasleitbtui'
txt[::2]


#3.Extract car names from the following text:
txt = 'MsaatmiazD'
txt[::2]


#4.Extract the residence area from the following text:
txt = "I'am John. I am from London"
txt[21:27]


#5.Write a Python program that takes a user input string and prints it in reverse order.
Name='Mirkomil'
reversed_Name=Name[::-1]
print(reversed_Name)


#6.Write a Python program that counts the number of vowels in a given string.
car='VolksWagen'

vovels='aeiou'

cnt=0

for i in car:
    if i in vovels:
        cnt=cnt+1
        
cnt


#7.Write a Python program that takes a list of numbers as input and prints the maximum value.
lst=[1,86,23,13,45]
sonlar=list(map(int,lst))

if sonlar:
    maksimum=max(sonlar)
    print('Eng katta qiymat:',maksimum)
else:
    print("Bo'sh.")


#8.Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
if 'non'=='non'[::-1]:
    print(True)
else:
    print(False)


#9.Write a Python program that extracts and prints the domain from an email address provided by the user.
email= "sultanovazizbek89@gmail.com"
domain=email.split('@')[1]
print("Domen:",domain)



#10.Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

letter=string.ascii_letters
digit=string.digits
symbols=string.punctuation

all_chars=letter+digit+symbols

length=int(input('Enter your pasword:'))

password=''.join(random.choice(all_chars) for _ in range(length))

print("Yaratilgan parol:",password)
