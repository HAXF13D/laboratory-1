a = int(input("Введите число: "))
count = 0
while a > 0:
    a = a // 10
    count += 1
print(f"Кол-во цифр в числе = {count}")
