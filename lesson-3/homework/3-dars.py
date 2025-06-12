#1.Create a list containing five different fruits and print the third fruit.
Mevalar=['Olma','Banan','Uzum','Nok','Shaftoli']
Mevalar[2]

#2.Create two lists of numbers and concatenate them into a single list.
l1=[1,2,3,4,5,6,7]
l2=[10,20,30,40,50]
l3=l1+l2
print('Combined:',l3)

#3.Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
l4=[30,40,50,60,70]
first=l4[0]
middle=l4[len(l4)//2]
last=l4[-1]
l5=[first,middle,last]
l5

#4.Create a list of your five favorite movies and convert it into a tuple.
list=[35,45,56,45,76]
tuple_name=tuple(list)
print(tuple_name)


#5.Given a list of cities, check if "Paris" is in the list and print the result.
cities=['Rio de Janeiro','Tokyo','Sydney','Paris','New York']

if cities.index('Paris'):
    print(True)
else:
    print(False)   

#6.Create a list of numbers and duplicate it without using loops.
numbers=[45,65,76,78 ,87,45]
duplicate=numbers.copy()
print(duplicate)


#7.Given a list of numbers, swap the first and last elements.
number=[23,34,54,76,86]
number[0],number[-1]=number[-1],number[0]
print(number)

#8.Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
n1=(1,2,3,4,5,6,7,8,9,10)
slice=n1[2:7]
print(slice)

#9.Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "green", "blue", "blue", "yellow", "blue", "orange"]
count_colors=colors.count('blue')
print("Ko'k rang:",count_colors)

#10.Given a tuple of animals, find the index of "lion".
animals = ("tiger", "lion", "elephant", "zebra")
index_of_lion = animals.index("lion")
print("Index of lion:", index_of_lion)


#11.Create two tuples of numbers and merge them into a single tuple.
number1=(1,2,3,4,5)
number2=(6,7,8,9)

sum_tuple=number1+number2
print('Combined:',sum_tuple)

#12.Given a list and a tuple, find and print their lengths.
country=['Uzbekistan']
country2=('Argentina')

lenght_country=len(country)
lenght_country2=len(country2)

print('Davlat:',lenght_country)
print('Davlat2:',lenght_country2)

#13.Create a tuple of five numbers and convert it into a list.

tuple1=(34,45,61,27,92)
list_name=list[tuple1]
print(list_name)

#14.Given a tuple of numbers, find and print the maximum and minimum values.

t=(23,43,45,67,65)
max_t=max(t)
min_t=min(t)

print('Maksimum',max_t)
print('Minimum',min_t)

#15.Create a tuple of words and print it in reverse order.
words = ('apple', 'banana', 'cherry')
reversed_words = words[::-1]

print("reversed tuple :",reversed_words)

