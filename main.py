# Boshlang'ich o'zgaruvchi: "fruits" deb nomlangan set o'zgaruvchi yaratamiz
fruits = {"apple", "banana"}

# 1-vazifa: "cherry" mevasini qo'shish
# add() metodi: Setga yangi element qo'shadi, agar element allaqachon mavjud bo'lsa, hech narsa qilmaydi
# Misol: {"apple", "banana"} + "cherry" -> {"apple", "banana", "cherry"}
result1 = fruits.add("cherry")
print("1-vazifa natijasi:", fruits)  # Natija: {'apple', 'banana', 'cherry'}

# 2-vazifa: "banana" mevasini o'chirish
# remove() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato (KeyError) chiqaradi
# Misol: {"apple", "banana", "cherry"} - "banana" -> {"apple", "cherry"}
result2 = fruits.remove("banana")
print("2-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry'}

# 3-vazifa: "kiwi" mevasini qo'shish
# add() metodi: Setga yangi element qo'shadi
# Misol: {"apple", "cherry"} + "kiwi" -> {"apple", "cherry", "kiwi"}
result3 = fruits.add("kiwi")
print("3-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi'}

# 4-vazifa: "apple" setda mavjudligini tekshirish
# in operatori: Element setda mavjud bo'lsa True, aks holda False qaytaradi
# Misol: "apple" in {"apple", "cherry", "kiwi"} -> True
result4 = "apple" in fruits
print("4-vazifa natijasi:", "yes" if result4 else "no")  # Natija: yes

# 5-vazifa: "tropicals" setini yaratish va "fruits" ga qo'shish
# update() metodi: Setga boshqa iterable (masalan, boshqa set) elementlarini qo'shadi
# Misol: {"apple", "cherry", "kiwi"} + {"pineapple", "banana"} -> {"apple", "cherry", "kiwi", "pineapple", "banana"}
tropicals = {"pineapple", "banana"}
result5 = fruits.update(tropicals)
print("5-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple', 'banana'}

# 6-vazifa: "banana" ni o'chirish (xatolik bermasi uchun)
# discard() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato chiqarmaydi
# Misol: {"apple", "cherry", "kiwi", "pineapple", "banana"} - "banana" -> {"apple", "cherry", "kiwi", "pineapple"}
result6 = fruits.discard("banana")
print("6-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}

# 7-vazifa: "fruits" va "tropicals" farqini topish
# difference() metodi: Birinchi setda bo'lib, ikkinchi setda bo'lmagan elementlarni qaytaradi
# Misol: {"apple", "cherry", "kiwi", "pineapple"} - {"pineapple", "banana"} -> {"apple", "cherry", "kiwi"}
result7 = fruits.difference(tropicals)
print("7-vazifa natijasi:", result7)  # Natija: {'apple', 'cherry', 'kiwi'}

# 8-vazifa: Yangi unique "fruits" nomli setga saqlash
# Setning o'zi elementlarni takrorlanmas qiladi, shuning uchun faqat yangi nom bilan saqlash kifoya
# Misol: {"apple", "cherry", "kiwi", "pineapple"} ni "unique_fruits" ga ko'chirish
unique_fruits = fruits
result8 = unique_fruits
print("8-vazifa natijasi:", result8)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}

# 9-vazifa: Barcha mevalarni alifbo bo'yicha tartiblash
# sorted() funksiyasi: Iterable (masalan, set) elementlarini alifbo tartibida ro'yxat sifatida qaytaradi
# Misol: {"apple", "cherry", "kiwi", "pineapple"} -> ['apple', 'cherry', 'kiwi', 'pineapple']
result9 = sorted(fruits)
print("9-vazifa natijasi:", result9)  # Natija: ['apple', 'cherry', 'kiwi', 'pineapple']

# 10-vazifa: Yakuniy holatni chop etish
# Faqat joriy setni chop qilish uchun hech qanday metod ishlatmaymiz
print("10-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}


# Boshlang'ich o'zgaruvchi: "colors" deb nomlangan set o'zgaruvchi yaratamiz
colors = {"red", "green", "blue"}

# 1-vazifa: "yellow" ni qo'shish
# add() metodi: Setga yangi element qo'shadi, agar element allaqachon mavjud bo'lsa, hech narsa qilmaydi
# Misol: {"red", "green", "blue"} + "yellow" -> {"red", "green", "blue", "yellow"}
result1 = colors.add("yellow")
print("1-vazifa natijasi:", colors)  # Natija: {'red', 'green', 'blue', 'yellow'}

# 2-vazifa: "green" ni o'chirish
# discard() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato chiqarmaydi
# Misol: {"red", "green", "blue", "yellow"} - "green" -> {"red", "blue", "yellow"}
result2 = colors.discard("green")
print("2-vazifa natijasi:", colors)  # Natija: {'red', 'blue', 'yellow'}

# 3-vazifa: "blue" ni tekshirish
# in operatori: Element setda mavjud bo'lsa True, aks holda False qaytaradi
# Misol: "blue" in {"red", "blue", "yellow"} -> True
result3 = "blue" in colors
print("3-vazifa natijasi:", "Found" if result3 else "Not Found")  # Natija: Found

# 4-vazifa: Yangi set yaratish
# extra_colors deb nomlangan yangi set yaratamiz, unda "black", "white", "red" ranglari bo'ladi
# Misol: extra_colors = {"black", "white", "red"}
extra_colors = {"black", "white", "red"}
print("4-vazifa natijasi:", extra_colors)  # Natija: {'black', 'white', 'red'}

# 5-vazifa: colors va extra_colors ni birlashtirish
# union() metodi: Ikkala setning barcha elementlarini birlashtirib, yangi set qaytaradi
# Takrorlanadigan elementlar faqat bir marta olinadi
# Misol: {"red", "blue", "yellow"} | {"black", "white", "red"} -> {"red", "blue", "yellow", "black", "white"}
result5 = colors.union(extra_colors)
print("5-vazifa natijasi:", result5)  # Natija: {'red', 'blue', 'yellow', 'black', 'white'}

# 6-vazifa: colors setidan extra_colors bilan umumiy bo'lmaganlarni olish
# difference_update() metodi: Setdan boshqa set bilan umumiy elementlarni o'chiradi, natija o'z setda saqlanadi
# Misol: {"red", "blue", "yellow"} - {"black", "white", "red"} -> {"blue", "yellow"}
result6 = colors.difference_update(extra_colors)
print("6-vazifa natijasi:", colors)  # Natija: {'blue', 'yellow'}

# 7-vazifa: colors va extra_colors kesishmasini topish
# intersection() metodi: Ikkala setda umumiy bo'lgan elementlarni yangi set sifatida qaytaradi
# Misol: {"blue", "yellow"} & {"black", "white", "red"} -> set() (umumiy element yo'q)
result7 = colors.intersection(extra_colors)
print("7-vazifa natijasi:", result7)  # Natija: set()

# 8-vazifa: Set uzunligini topish
# len() funksiyasi: Setdagi elementlar sonini qaytaradi
# Misol: {"blue", "yellow"} -> 2
result8 = len(colors)
print("8-vazifa natijasi:", result8)  # Natija: 2

# 9-vazifa: Bo'sh setni nusxalab yangi set yaratish va tozalash
# copy() metodi: Setning nusxasini yaratadi
# clear() metodi: Setdagi barcha elementlarni o'chiradi, bo'sh set qoldiradi
# Misol: {"blue", "yellow"} nusxasi -> bo'sh set
new_set = colors.copy()
new_set.clear()
print("9-vazifa natijasi:", new_set)  # Natija: set()

# 10-vazifa: Har bir bo'sh joydan so'ng setni chop etish
# Faqat joriy setni chop qilish uchun hech qanday metod ishlatmaymiz
print("10-vazifa natijasi:", colors)  # Natija: {'blue', 'yellow'}


students = {'Ali', 'Vali', 'Sami'}

added_student = 'Aziz'
students.add(added_student)
print(f"Yangi talaba qo'shildi: {added_student}", students)

removed_student = 'Sami'
students.remove(removed_student)
print(f"Talaba o'chirildi: {removed_student}", students)

result = 'Jamshid' in students
print(f"{result}")

added_student2 = 'Jamshid'
students.add(added_student2)
print(f"Yangi talaba qo'shildi: {added_student2}", students)

new_students = {'Vali', 'Diyor'}
students.update(new_students)
print("Yangi talabalar qo'shildi:", students)

z = students.difference(new_students)
print(z)

graduates = {'Ali', 'Jamshid'}
print(f"9-vazifa: {graduates}")

x = graduates.symmetric_difference(students)
print(f"10-vazifa: {x}")