print("Введите текст:")
text = input()
n = len(text) + 4

i = 0
while i < n:
    print('*', end='')
    i += 1
print()

print('* ' + text + ' *')

i = 0
while i < n:
    print('*', end='')
    i += 1
print()