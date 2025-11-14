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


# #3-masala
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


# #4-masala
numbers = {1, 2, 3, 4}

added_num = 5
numbers.add(added_num)
print(f"(1-vazifa): Yangi raqam qo'shildi: {added_num}", numbers)

removed_num = 2
numbers.discard(removed_num)
print(f"(2-vazifa): Raqam o'chirildi: {removed_num}", numbers)

check_num = 10
z = check_num in numbers
print(f"(3-vazifa): {z}")

more_nums = {3, 6, 7}
print(f"4-vazifa: {more_nums}")

numbers.update(more_nums)
print(f"(5-vazifa): Raqamlar yangilandi:", numbers)

common_nums = numbers.intersection(more_nums)
print(f"(6-vazifa): Umumiy raqamlar:", common_nums)

farq = numbers.difference(more_nums)
print(f"(7-vazifa): Farq:", farq)

uni = numbers.union(more_nums)
print(f"(8-vazifa): Birlashma:", uni)

max(numbers)
print(f"(9-vazifa): Maksimal raqam:", max(numbers))
min(numbers)
print(f"(10-vazifa): Minimal raqam:", min(numbers))


# 5-Masala: Hayvonlar to'plami
animals = {'cat', 'dog', 'fish'}

animals.add('rabbit')
print(animals)

animals.remove('dog')
print(animals)

print('parrot' in animals)

animals.add('parrot')
print(animals)

more_animals = {'lion', 'cat'}
print(more_animals)

animals.update(more_animals)
print(animals)

print(animals.difference(more_animals))

print(sorted(animals))

print(len(animals))
print(animals)

# 6-Masala: Xarid savati
cart = {'milk', 'bread', 'cheese'}

cart.add('butter')
cart.remove('milk')
print('jam' in cart)
cart.add('jam')
new_items = {'bread', 'yogurt'}
cart.update(new_items)
other_cart = {'bread', 'yogurt', 'eggs'}
print(cart.difference(other_cart))
print(cart.intersection(new_items))
print(bool(cart))
print(cart)

# 7-Masala: Fanlar ro'yxati
subjects = {'Math', 'Physics'}

subjects.add('Biology')
subjects.discard('Math')
print('Chemistry' in subjects)
subjects.add('Chemistry')
extra = {'History', 'Physics'}
print(subjects.union(extra))
subjects_copy = subjects.copy()
subjects_copy.add('Geography')
print(subjects.symmetric_difference(subjects_copy))
print(subjects)

# 8-Masala: Shaharlar seti
cities = {'Tashkent', 'Samarkand'}

cities.add('Bukhara')
cities.remove('Samarkand')
print('Khiva' in cities)
cities.add('Khiva')
uzbek_cities = {'Andijan', 'Namangan', 'Tashkent'}
cities.update(uzbek_cities)
print(cities.difference(uzbek_cities))
print(cities.intersection(uzbek_cities))
print(sorted(cities))
print(len(cities))
print(cities)

# 9-Masala: Brendlar seti
brands = {'Nike', 'Adidas'}

brands.add('Puma')
brands.discard('Adidas')
print('Reebok' in brands)
brands.add('Reebok')
local_brands = {'Sabr', 'Nike'}
print(brands.union(local_brands))
print(brands.difference(local_brands))
brands_copy = brands.copy()
brands_copy.clear()
print(brands)
print(brands_copy)

# 10-Masala: Kitob nomlari bilan ishlash
books = {'1984', 'Hamlet', 'Inferno'}

books.add('Animal Farm')
books.remove('Inferno')
print('Hamlet' in books)
books.add('Fahrenheit 451')
new_books = {'1984', 'Dune'}
books.update(new_books)
print(books.difference(new_books))
print(books.intersection(new_books))
print(sorted(books))
print(books)

# 11-Masala: Mehmonlar ro'yxatini boshqarish
invited = {'Ali', 'Vali', 'Salim'}
arrived = {'Vali', 'Sami'}

invited.add('Aziza')
print(invited.intersection(arrived))
print(invited.difference(arrived))
print(invited.union(arrived))
invited.clear()
arrived.discard('Sami')
arrived.add('Sardor')
print(arrived.difference(invited))
print(len(arrived))
print(invited)
print(arrived)

# 12-Masala: Online kursga yozilganlar
udemy = {'Alisher', 'Dilshod', 'Malika'}
coursera = {'Malika', 'Zafar'}

udemy.add('Shahnoza')
print(udemy.intersection(coursera))
print(coursera.difference(udemy))
print(udemy.union(coursera))
udemy_copy = udemy.copy()
udemy_copy.remove('Dilshod')
print(udemy.symmetric_difference(coursera))
print(sorted(udemy.union(coursera)))
print(len(udemy))
print(len(coursera))
print(udemy)
print(coursera)

# 13-Masala: Bo'sh ish o'rinlariga ariza topshirganlar
it_vacancy = {'Azamat', 'Javlon', 'Sarvar'}
design_vacancy = {'Javlon', 'Sabrina'}

it_vacancy.add('Kamila')
print(it_vacancy.difference(design_vacancy))
print(it_vacancy.intersection(design_vacancy))
print(design_vacancy.difference(it_vacancy))
all_applicants = it_vacancy.union(design_vacancy)
print(all_applicants)
combined = all_applicants.copy()
combined.discard('Sarvar')
print(it_vacancy.symmetric_difference(design_vacancy))
print(len(it_vacancy))
print(len(design_vacancy))
print(sorted(all_applicants))

# 14-Masala: Tibbiy tekshiruvdan o'tganlar
students = {'Ali', 'Soliha', 'Bobur'}
checked = {'Bobur', 'Ali'}

checked.add('Gulbahor')
print(students.difference(checked))
print(sorted(checked))
print(students.union(checked))
print(len(checked))
checked_copy = checked.copy()
checked_copy.discard('Ali')
print(students.symmetric_difference(checked))
print(bool(students))
print(bool(checked))
print(students.intersection(checked))
print(students)
print(checked)

# 15-Masala: Sayohat qilgan o'quvchilar
toshkent_trip = {'Olim', 'Rustam', 'Ziyoda'}
samarkand_trip = {'Ziyoda', 'Kamola'}

toshkent_trip.add('Nodira')
print(toshkent_trip.intersection(samarkand_trip))
print(toshkent_trip.difference(samarkand_trip))
print(toshkent_trip.union(samarkand_trip))
print(toshkent_trip.symmetric_difference(samarkand_trip))
toshkent_trip.discard('Ziyoda')
samarkand_trip.discard('Ziyoda')
trip_copy = toshkent_trip.copy()
trip_copy.clear()
print(len(toshkent_trip))
print(len(samarkand_trip))
print(sorted(toshkent_trip.union(samarkand_trip)))
print(toshkent_trip)
print(samarkand_trip)

# 16-Masala: Restoranga buyurtma berganlar
online_orders = {'Ulugbek', 'Shoira', 'Ibrohim'}
cash_orders = {'Ibrohim', 'Dilshod'}

online_orders.add('Muzaffar')
print(cash_orders.difference(online_orders))
print(online_orders.intersection(cash_orders))
print(online_orders.symmetric_difference(cash_orders))
print(sorted(online_orders.union(cash_orders)))
orders_copy = online_orders.copy()
orders_copy.clear()
print(len(online_orders))
print(len(cash_orders))
cash_orders.discard('Dilshod')
print(online_orders)
print(cash_orders)

# 17-Masala: Sport musobaqasi qatnashchilari
football = {'Otabek', 'Ali'}
basketball = {'Ali', 'Javohir'}

football.add('Farrux')
print(football.intersection(basketball))
print(football.difference(basketball))
print(basketball.difference(football))
print(football.union(basketball))
print(football.symmetric_difference(basketball))
football.discard('Ali')
basketball.discard('Ali')
basketball_copy = basketball.copy()
basketball_copy.clear()
print(football)
print(basketball)
print(basketball_copy)

# 18-Masala: Elektron pochta ro'yxati
registered = {'a@gmail.com', 'b@gmail.com', 'c@gmail.com'}
verified = {'b@gmail.com', 'c@gmail.com', 'd@gmail.com'}

registered.add('e@gmail.com')
print(registered.difference(verified))
print(registered.intersection(verified))
print(registered.union(verified))
print(registered.difference(verified))
print(registered.symmetric_difference(verified))
print(sorted(registered.union(verified)))
print(len(registered))
print(len(verified))
registered.discard('c@gmail.com')
verified.discard('c@gmail.com')
print(registered)
print(verified)

# 19-Masala: Darsga kechikkanlar
present = {'Asilbek', 'Nodir', 'Gulnoza'}
late = {'Gulnoza', 'Madina'}

present.add('Madina')
print(late.difference(present))
print(present.difference(late))
print(present.union(late))
print(present.symmetric_difference(late))
present.discard('Asilbek')
present_copy = present.copy()
present_copy.clear()
print(sorted(present.union(late)))
print(present)
print(late)

# 20-Masala: Kutubxonadan kitob olganlar
taken = {'Lola', 'Shoxrux', 'Muhammad'}
returned = {'Muhammad', 'Lola'}

taken.add('Suhrob')
print(taken.difference(returned))
print(len(returned))
print(taken.union(returned))
print(taken.difference(returned))
print(taken.symmetric_difference(returned))
taken.discard('Shoxrux')
taken_copy = taken.copy()
print(sorted(taken.union(returned)))
print(taken)
print(returned)