n = int(input("Введите неотрицательное целое число N: "))

if n < 0:
    print("Ну не надо вводить отрицательные числа")
else:
    f = 1
    for i in range(2, n + 1):
        f *= i
    print(f"{n}! = {f}")