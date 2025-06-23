
#1
import math

class Circle:
    def __init__(self,radius):
       self.radius=radius
       
    def area(self):
        return math.pi*self.radius**2
    
    def perimetr(self):
        return 2*math.pi*self.radius
    
c=Circle(5)

print("Maydon:",c.area())
print("Perimetr:",c.perimetr())

#2
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth

p1=Person('Aziz','Uzbekistan','09.01.2002')

#3
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return 


calc = Calculator()

# Test qilish
print("Add:", calc.add(10, 5))
print(" Subtract:", calc.subtract(9, 3))
print(" multiply:", calc.multiply(4, 7))
print(" divide:", calc.divide(20, 4))
print(" divide (nolga):", calc.divide(10, 0))


#4
import math


class Shape:
    def area(self):
        raise NotImplementedError("Maydon hisoblash metodi aniqlanmagan!")

    def perimeter(self):
        raise NotImplementedError("Perimetr hisoblash metodi aniqlanmagan!")


# Circle klassi: doira
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Square klassi: kvadrat
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side



class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Sinov uchun ishlatamiz:
if __name__ == "__main__":
 
    circle = Circle(radius=5)
    print("Circle:")
    print("  Area:", round(circle.area(), 2))
    print("  Perimeter:", round(circle.perimeter(), 2))

  
    square = Square(side=4)
    print("\nSquare:")
    print("  Area:", square.area())
    print("  Perimeter:", square.perimeter())


    triangle = Triangle(a=3, b=4, c=5)
    print("\nTriangle:")
    print("  Area:", round(triangle.area(), 2))
    print("  Perimeter:", triangle.perimeter())

#4


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

 
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
        

   
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(13)
    bst.insert(18)

    print("BST Inorder Traversal:")
    bst.inorder_traversal(bst.root)  # 3 5 7 10 13 15 18

    print("\n\nSearching 13:", bst.search(13))  # True
    print("Searching 9:", bst.search(9))        # False

#5

class Stack:
    def __init__(self):
        self.items = []  # bo‘sh ro‘yxat — stack saqlovchi

    def push(self, item):
        self.items.append(item)  # elementni oxiriga qo‘shish

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # oxirgi elementni olib tashlaydi va qaytaradi
        else:
            return None  # yoki raise Exception('Stack is empty')

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # so‘nggi elementni ko‘rsatadi (olmaydi)
        else:
            return None

    def size(self):
        return len(self.items)


#  Namuna ishlatish
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stackdan olingan:", s.pop())   # 30
    print("Yuqoridagi element:", s.peek())  # 20
    print("Stack uzunligi:", s.size())      # 2
    print("Stack bo‘shmi?", s.is_empty())   # False


#7

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

  
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    
    def delete(self, data):
        current = self.head
        prev = None

        while current is not None:
            if current.data == data:
                if prev is None:
                    # o‘chirilayotgan tugun — head
                    self.head = current.next
                else:
                    prev.next = current.next
                return  # birinchi mos kelgan tugunni o‘chiradi
            prev = current
            current = current.next

    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    print("Boshlang‘ich ro‘yxat:")
    ll.display()  # 10 -> 20 -> 30 -> None

    ll.delete(20)
    print("20 o‘chirildi:")
    ll.display()  # 10 -> 30 -> None

    ll.delete(10)
    print("10 o‘chirildi:")
    ll.display()  # 30 -> None

    ll.delete(30)
    print("30 o‘chirildi:")
    ll.display()  # None


#8

class ShoppingCart:
    def __init__(self):
        self.items = {}  # Lug'at: mahsulot_nomi -> {"price": narx, "quantity": miqdor}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] -= quantity
            if self.items[name]["quantity"] <= 0:
                del self.items[name]

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def display_cart(self):
        if not self.items:
            print("Savat bo‘sh.")
            return
        print(" Savatdagi mahsulotlar:")
        for name, info in self.items.items():
            print(f"{name}: {info['quantity']} x ${info['price']:.2f}")
        print(f" Umumiy: ${self.calculate_total():.2f}\n")

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("olma", 1.2, 3)
    cart.add_item("banan", 0.8, 5)
    cart.add_item("olma", 1.2, 2)   # mavjud olma sonini oshiradi

    cart.display_cart()

    cart.remove_item("banan", 2)   # 2 dona banan olib tashlandi
    cart.display_cart()

    cart.remove_item("banan", 3)   # qolgan bananlar ham o‘chirildi
    cart.display_cart()


#9
class Stack:
    def __init__(self):
        self.items = []  

    def push(self, item):
        self.items.append(item)
        print(f"{item} stackga qo‘shildi.")

    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"{removed} stackdan o‘chirildi.")
            return removed
        else:
            print("Stack bo‘sh — hech narsa o‘chirilmadi.")
            return None

    def display(self):
        if not self.is_empty():
            print(" Stack holati (yuqoridan pastga):")
            for item in reversed(self.items):
                print(f"| {item} |")
            print("--------")
        else:
            print(" Stack bo‘sh.")

    def is_empty(self):
        return len(self.items) == 0



if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    s.display()

    s.pop()
    s.display()

    s.pop()
    s.pop()
    s.pop()  # bo‘sh stackdan olish harakati


#10

class Queue:
    def __init__(self):
        self.items = []  

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} navbatga qo‘shildi.")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)  # navbat boshidan o‘chirish
            print(f"{removed} navbatdan olib tashlandi.")
            return removed
        else:
            print("Navbat bo‘sh — hech narsa olib tashlanmadi.")
            return None

    def display(self):
        if not self.is_empty():
            print(" Navbat holati (chapdan o‘ngga):")
            print(" -> ".join(str(item) for item in self.items))
        else:
            print("📭 Navbat bo‘sh.")

    def is_empty(self):
        return len(self.items) == 0



if __name__ == "__main__":
    q = Queue()

    q.enqueue("Olma")
    q.enqueue("Banan")
    q.enqueue("Anor")

    q.display()

    q.dequeue()
    q.display()

    q.dequeue()
    q.dequeue()
    q.dequeue()  # Bo‘sh navbatdan olish

#11

class Bank:
    def __init__(self):
        self.accounts = {} 

    def create_account(self, account_number, name, initial_deposit=0):
        if account_number in self.accounts:
            print("⚠ Bu hisob raqami allaqachon mavjud.")
        else:
            self.accounts[account_number] = {"name": name, "balance": initial_deposit}
            print(f" Hisob ochildi: {name}, Raqam: {account_number}, Boshlang‘ich balans: ${initial_deposit}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f" {amount}$ qo‘shildi. Yangi balans: ${self.accounts[account_number]['balance']}")
        else:
            print(" Hisob topilmadi.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f" {amount}$ yechildi. Yangi balans: ${self.accounts[account_number]['balance']}")
            else:
                print(" Hisobda yetarli mablag‘ yo‘q.")
        else:
            print(" Hisob topilmadi.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            print(f"📊 Balans: ${balance}")
            return balance
        else:
            print(" Hisob topilmadi.")
            return None

    def list_customers(self):
        print(" Mijozlar ro‘yxati:")
        for acc_num, info in self.accounts.items():
            print(f"{acc_num} → {info['name']} (${info['balance']})")



if __name__ == "__main__":
    my_bank = Bank()

    my_bank.create_account("1001", "Akmal", 500)
    my_bank.create_account("1002", "Dilshod", 1000)

    my_bank.deposit("1001", 200)
    my_bank.withdraw("1002", 300)
    my_bank.check_balance("1001")

    my_bank.list_customers()

    my_bank.withdraw("1002", 800)  # Yetarli mablag‘ yo‘q holati
    my_bank.deposit("9999", 100)   # Noto‘g‘ri hisob raqami


print(p1.name,p1.country,p1.date_of_birth)
