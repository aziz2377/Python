#1
try:
    5/0
except ZeroDivisionError:
    print('Error')

#2

try:
    user_input = input("Please enter an integer: ")
    number = int(user_input)  
    print(f"You entered the integer: {number}")
except ValueError:
    print("Error: That is not a valid integer.")

#3
# Python program to open a file and handle FileNotFoundError

file_name = "example.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")


#4
try:
    a=input('1-son')
    b=input('2-son')

    num1=float(a)
    num2=float(b)
    
    
    print(f"Yig'indisi: {num1 + num2}")


except ValueError:
    print("Faqat son kiriting.")


#5
file_name = "sample.txt"

try:
    with open(file_name, 'r') as file:
        content=file.read()
        print("File content:\n",content)
except PermissionError:
    print(f"Permission denied: You do not have permission to read the file '{file_name}'.")
except FileNotFoundError:
    print(f"File not found: '{file_name}' does not exist.")


#6
my_list=[10,20,30,40]

index = int(input("Indeks kiriting (0-4 oralig‘ida): "))

try:
    value=my_list[index]
    print("Element:",value)
except IndexError:
    print("Xatolik: Bunday indeks mavjud emas.")

#7 Python program to handle KeyboardInterrupt when user cancels input

try:
    user_input = input("Please enter a number: ")
    number = float(user_input)
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("\nInput cancelled by user (KeyboardInterrupt).")
except ValueError:
    print("Invalid input: please enter a valid number.")

#8
try:
    n=input('Son kiriting:')
    number=float(n)
    print(f"Siz kiritgan son:{number}")
except KeyboardInterrupt:
    print("\nSiz kiritishni bekor qildingiz.")

#9
try:
    x=5/0
except ArithmeticError as A :
    print("ArithmeticError:",A)

#10

file_name = 'example.txt'

try:
    with open(file_name, mode='r', encoding='utf-8') as f:
        content = f.read()
        print("Fayl muvaffaqiyatli o'qildi.")
        print(content)

except UnicodeDecodeError:
    print("⚠️ UnicodeDecodeError: Faylni o‘qishda kodlash bilan bog‘liq muammo yuz berdi.")

#11
my_list=[1,2,3]

try:
    my_list.upper()
except AttributeError:
    print('Atribut xato')


    
#1

file_name = "sample.txt"  # O‘qiladigan fayl nomi

try:
    with open(file_name, mode='r', encoding='utf-8') as f:
        content = f.read()
        print(" Fayl mazmuni:")
        print(content)
except FileNotFoundError:
    print(" Fayl topilmadi.")
except UnicodeDecodeError:
    print(" Kodlash bilan bog‘liq muammo (UnicodeDecodeError).")


#2

file_name = "example.txt"  # O‘qiladigan fayl nomi

try:
    n = int(input("Nechta birinchi satrni o‘qishni xohlaysiz? "))

    with open(file_name, mode='r', encoding='utf-8') as f:
        for i in range(n):
            line = f.readline()
            if not line:  # Fayl tugagan bo‘lsa
                break
            print(f"{i+1}: {line.strip()}")

except FileNotFoundError:
    print(" Fayl topilmadi.")
except UnicodeDecodeError:
    print(" Kodlash bilan bog‘liq muammo (UnicodeDecodeError).")
except ValueError:
    print(" Iltimos, butun son kiriting.")

#3

file_name = "example.txt"  # Fayl nomi

try:
   
    text = input("Faylga qanday matn qo‘shmoqchisiz? ")

   
    with open(file_name, mode='a', encoding='utf-8') as f:
        f.write(text + "\n")  # Yangi qatordan yozish

    
    with open(file_name, mode='r', encoding='utf-8') as f:
        content = f.read()
        print("\n📄 Yangilangan fayl mazmuni:")
        print(content)

except FileNotFoundError:
    print(" Fayl topilmadi.")
except IOError:
    print(" Fayl bilan ishlashda xatolik yuz berdi.")

#4

from collections import deque


filename = input("Fayl nomini kiriting: ")
n = int(input("Oxirdan nechta qator o‘qilsin? "))

try:
    with open(filename, "r") as file:
      
        last_lines = deque(file, maxlen=n)

    print(f"\n {filename} faylining oxirgi {n} qatori:")
    for line in last_lines:
        print(line.strip())

except FileNotFoundError:
    print(" Bunday fayl topilmadi.")
except Exception as e:
    print(f" Xatolik yuz berdi: {e}")

#5
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r") as file:
        
        lines_list = [line.strip() for line in file]


    print("\n📄 Fayldagi barcha satrlar (ro‘yxat ko‘rinishida):")
    for i, line in enumerate(lines_list, start=1):
        print(f"{i}: {line}")

except FileNotFoundError:
    print("❌ Bunday fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")



#6

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r") as file:
        # Butun faylni bitta matnga yig‘ish
        content = ""
        for line in file:
            content += line  # har bir qatorni qo‘shib boramiz

    # Natijani chiqarish
    print("\n📄 Fayl mazmuni (bitta o‘zgaruvchida):\n")
    print(content)

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")




#7
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines]

    print("\n📋 Fayl satrlaridan olingan ro‘yxat:")
    print(cleaned_lines)

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")

#8
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r") as file:
        words = file.read().split()

    if not words:
        print("❌ Faylda so‘zlar topilmadi.")
    else:
        max_len = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_len]

        print(f"\n🔍 Eng uzun so‘z uzunligi: {max_len}")
        print("📝 Eng uzun so‘z(lar):")
        for word in longest_words:
            print(f"• {word}")

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik: {e}")



#9
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r") as file:
        line_count = 0
        for line in file:
            line_count += 1

    print(f"\n📄 Fayldagi qatorlar soni: {line_count}")

except FileNotFoundError:
    print("❌ Bunday fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")

#10
from collections import Counter
import re

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    # So‘zlarga ajratish va tinish belgilarni olib tashlash
    words = re.findall(r'\b\w+\b', text.lower())

    # So‘z chastotasi
    word_freq = Counter(words)

    print("\n📊 So‘zlar chastotasi:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik: {e}")

#11
import os


filename = input("Fayl nomini kiriting: ")


if os.path.isfile(filename):
    size = os.path.getsize(filename)
    print(f"📄 Fayl hajmi: {size} bayt")
else:
    print("❌ Bunday fayl topilmadi yoki bu katalog.")


#12
fruits = ['apple', 'banana', 'cherry', 'mango']


filename = "fruits.txt"

try:
    with open(filename,'w') as file:
        for fruit in fruits:
            file.write(fruit+"\n")
    
    print(f"Ro'yhat '{filename}'fayliga muvaffaqiyatli yozildi.")

except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")


#13

# 1. Foydalanuvchidan fayl nomlarini olish
source_file = input("Manba fayl nomi: ")
destination_file = input("Yangi (nusxa) fayl nomi: ")

try:
    # 2. Fayllarni ochish va ma’lumotni nusxalash
    with open(source_file, "r") as src:
        with open(destination_file, "w") as dest:
            for line in src:
                dest.write(line)

    print(f"✅ '{source_file}' fayli muvaffaqiyatli '{destination_file}' ga nusxalandi.")

except FileNotFoundError:
    print("❌ Manba fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")


#14

# 1. Fayl nomlarini olish
file1 = input("1-fayl nomi: ")
file2 = input("2-fayl nomi: ")

try:
    # 2. Fayllarni ochish
    with open(file1, "r") as f1, open(file2, "r") as f2:
        # 3. Har bir qatorni birlashtirish
        with open("combined.txt", "w") as out:
            for line1, line2 in zip(f1, f2):
                combined = line1.strip() + " " + line2.strip()
                out.write(combined + "\n")

    print("✅ Fayllar satrma-satr muvaffaqiyatli birlashtirildi → combined.txt")

except FileNotFoundError:
    print("❌ Fayllardan biri topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")


#15
import random

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    if not lines:
        print("⚠️ Fayl bo‘sh.")
    else:
        random_line = random.choice(lines)
        print("🎲 Tasodifiy qator:")
        print(random_line.strip())

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")


#16
filename = input("Fayl nomini kiriting: ")

try:
    # 1. Faylni ochamiz
    file = open(filename, "r")

    # 2. Holatini tekshiramiz
    if file.closed:
        print("📄 Fayl yopilgan.")
    else:
        print("📂 Fayl hozircha ochiq.")

    # 3. Endi uni yopamiz
    file.close()

    # 4. Yana tekshiramiz
    if file.closed:
        print("✅ Fayl endi yopildi.")
    else:
        print("⚠️ Fayl hanuz ochiq.")

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")


#17
#1. Fayl nomini so‘rash
source_file = input("Manba fayl nomini kiriting: ")
output_file = input("Yangi fayl nomini kiriting: ")

try:
    # 2. Faylni o‘qish
    with open(source_file, "r") as file:
        lines = file.readlines()

    # 3. Qatorlarni tozalash
    cleaned_lines = [line.strip() for line in lines]

    # 4. Bitta matnga birlashtirish (bo‘sh joy bilan)
    final_text = " ".join(cleaned_lines)

    # 5. Yangi faylga yozish
    with open(output_file, "w") as output:
        output.write(final_text)

    print(f"✅ '{source_file}' dan barcha yangi qator belgilar olib tashlandi → '{output_file}' fayliga yozildi.")

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")


#18
import re

# 1. Foydalanuvchidan fayl nomini olish
filename = input("Fayl nomini kiriting: ")

try:
    # 2. Faylni ochish va o‘qish
    with open(filename, "r") as file:
        text = file.read()

    # 3. So‘zlarni ajratish (vergul va tinish belgilarsiz)
    words = re.findall(r'\b\w+\b', text)

    # 4. So‘zlar sonini hisoblash
    word_count = len(words)

    # 5. Natijani chiqarish
    print(f"\n📊 So‘zlar soni: {word_count}")

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik: {e}")


#19
import glob

# 1. .txt fayllarni topamiz
files = glob.glob("*.txt")

# 2. Belgilarni yig‘ish uchun list
characters = []

try:
    # 3. Har bir faylni o‘qish va belgilarni yig‘ish
    for filename in files:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            for char in text:
                characters.append(char)

    # 4. Natijani chiqarish
    print(f"\n✅ {len(files)} ta fayldan jami {len(characters)} ta belgi olindi.")
    print("🔠 Dastlabki 100 belgi:", characters[:100])

except FileNotFoundError:
    print("❌ Fayl topilmadi.")
except Exception as e:
    print(f"⚠️ Xatolik yuz berdi: {e}")


#20
import string

# 1. Lotin alifbosidagi katta harflar
letters = string.ascii_uppercase  # 'A' to 'Z'

# 2. Fayllarni yaratish
for letter in letters:
    filename = f"{letter}.txt"
    try:
        with open(filename, "w") as file:
            file.write(f"This is file {filename}")
        print(f"✅ {filename} yaratildi.")
    except Exception as e:
        print(f"⚠️ {filename} fayl yaratishda xatolik: {e}")



#21
import string

# 1. Harflarni olish
alphabet = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']

# 2. Nechta harf bir qatorda bo‘lishini so‘rash
n = int(input("Har bir qatorda nechta harf bo‘lsin? (masalan: 5) "))

# 3. Faylga yozish
with open("alphabet_block.txt", "w") as file:
    for i in range(0, len(alphabet), n):
        block = alphabet[i:i+n]
        file.write(" ".join(block) + "\n")

print("✅ 'alphabet_block.txt' fayliga yozildi.")




