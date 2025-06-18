
#1
txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'uiaeoAOIUE'
cnt = 2
while cnt < len(txt):
    if txt[cnt] not in vowels:
        txt = txt[:cnt+1] + '_' + txt[cnt +1:]
        vowels += txt[cnt]
        cnt = cnt + 4
        #continue
    cnt = cnt + 1
    
txt[:-1]

#2
n=int(input('Enter number:'))

for i in range(n): 
    0 <= i < n
    print(i**2)

#1
i=1
while i<=10:
    print(i)
    i+=1


#2
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

#3
n=int(input('Enter number'))
total=0
    
for i in range(1,n+1):
    total +=i
print(total)
        
#4
n=int(input())

for i in range(1,11):
    print(f'{i*n}')



#5
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break           
    if num > 150:
        continue        
    if num % 5 == 0:
        print(num)    


#6
n=75869
cnt=0

while n !=0:
    n=n//10
    cnt +=1

print("Raqamlar soni:", cnt)     



#7
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()


#8
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1,-1,-1):
    print(list1[i])


#9
for i in range(-10,0):
    print(i)


#10
i=0

while i < 6:
    if i==5:

        print('Done!')  
        break  
    print(i)
    i +=1


#11

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            return False
    return True

# Oraliq
start = 25
end = 50

print("Prime numbers between", start, "and", end, "are:")

for i in range(start, end + 1):
    if is_prime(i):
        print(i)


#12
n = int(input("Nechta Fibonacci sonini ko‘rmoqchisiz? "))

a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


#13
num = int(input("Enter number "))

factorial = 1

if num < 0:
    print("Manfiy sonlar uchun faktorial mavjud emas.")
else:
    for i in range(1,num+1):
        factorial*= i
        print(f"{num}!={factorial}")


#14
from collections import Counter
list1 = [1, 1, 2]
list2 = [2, 3, 4]

c1 = Counter(list1)
c2 = Counter(list2)


only_in_1 = c1 - c2
only_in_2 = c2 - c1


result = list(only_in_1.elements()) + list(only_in_2.elements())

print(result)


from collections import Counter

def not_common_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)

    only_in_1 = c1 - c2
    only_in_2 = c2 - c1

    return list(only_in_1.elements()) + list(only_in_2.elements())
print(not_common_elements([1, 2, 3], [4, 5, 6]))


from collections import Counter
list1 = [1, 1, 2,3,4,2]
list2 = [1, 3, 4,5]

c1 = Counter(list1)
c2 = Counter(list2)

# Har bir ro'yxatdagi faqat o'ziga xos elementlar (boshqada yo'q bo'lganlar)
only_in_1 = c1 - c2
only_in_2 = c2 - c1

# Natijani birlashtiramiz
result = list(only_in_1.elements()) + list(only_in_2.elements())

print(result)



