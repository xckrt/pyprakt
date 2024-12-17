import math
a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
print("Числа из массива меньше 15:")
result = [x for x in a if x < 15]
print(result)
number = float(input("Введите число: "))
if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")


def calculator():
    print("Выберите операцию: +, -, *, /")
    operation = input("Введите операцию: ")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if operation == "+":
        print(f"Результат: {num1 + num2}")
    elif operation == "-":
        print(f"Результат: {num1 - num2}")
    elif operation == "*":
        print(f"Результат: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Результат: {num1 / num2}")
        else:
            print("Ошибка: деление на ноль!")
    else:
        print("Ошибка: некорректная операция")

print("Калькулятор")
calculator()
print("Отсчет от 10 до 1")
for i in range(10, 0, -1):
    print(i)


print("Решение квадратного уравнения")
def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x,
    else:
        return "Нет решений"


a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

solutions = solve_quadratic(a, b, c)
print(f"Решения: {solutions}")
