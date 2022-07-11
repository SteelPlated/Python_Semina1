'''
2. Напишите программу, которая на вход принимает 5
чисел и находит максимальное из них.

Примеры:

- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90'''

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
max_number=a
if max_number<b:
    max_number=b
if max_number<c:
    max_number=c
if max_number<d:
    max_number= d
if max_number<e:
    max_number=e
print(max_number)

'''a = list(map(int, input().split()))
max_number = a[0]
for i in a:
if i > max_number:
max_number = i
print(max_number)'''