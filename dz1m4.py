# На вход подается строка, все символы находятся в нижнем регистре и без пробелов. Напишите функцию, которая будет возвращать True, 
#если строка является палиндромом и False, если строка палиндромом не является.
# Примечание: палиндром — это строка, которая читается одинаково как слева направо, так и справа налево
# Пример входных данных 1:
# лепсспел
# Пример выходных данных 1:
# True
# Пример входных данных 2:
# helloworld
# Пример выходных данных 2:
# False

def palindrome(s):
    s = s[::-1]
s = str(input())
if s == s[::-1]:
    print("True")
else:
    print("False")