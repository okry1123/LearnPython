__author__ = 'apple'
age = 18

# ----if else----
if age >= 18:
    print("you age is", age)
    print("you are adult")
elif age >= 14:
    print("you age is", age)
    print("you are teenage")
else:
    print("you age is", age)
    print("you are child")
# --------

# ----简写if----
if age:
    print(True)
# --------

# ----for each----
fruits = ['Apple', 'Orange', 'Watermelon']

for fruit in fruits:
    print(fruit)

numbers = range(101)

for number in numbers:
    print(number)

sum = 0
for n in numbers:
    sum += n
print(sum)

for x in range(3):
    print('x')
# --------

# ----while----
n = 50
while n > 0:
    print(n)
    n = int(n / 2)

# 死循环
# while 1:
#     print('while')
# --------
