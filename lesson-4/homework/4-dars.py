#1
my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", asc_sorted)


desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", desc_sorted)


#2
d={0: 10, 1: 20}
d['2']=30
d

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict={**dic1,**dic2,**dic3}
print(new_dict)


#4
n=int(input('Enter number'))
kvadrat_lugat={}

for x in range(1,n+1):
    kvadrat_lugat[x]=x*x
print(kvadrat_lugat)


#5
squares = {x: x**2 for x in range(1, 16)}
print(squares)


#1
my_set={1,3,4,5}
print(my_set)

#2
my_set = {10, 20, 30, 40, 50}

for item in my_set:
    print(item)


#3
my_set1={'apple','banana'}
my_set1.add('cherry')
print('Updated set:',my_set1)


#4
car_set={'BMW','Mercedes','Audi'}
car_set.remove('Audi')
print('Removed:',car_set)


#5
mevaset = {"olma", "banan", "shaftoli"}
element = "banan"
if element in mevaset:
    mevaset.remove(element)
    print(mevaset)
