__author__ = 'apple'
# ----build-in function basic----
print('# ----built-in function basic----')
print(abs(-1))
print(int(12.3))
print(str(12))
print(float(12))
print(bool(12))
# see more built-in function here https://docs.python.org/3.4/library/functions.html#cmp
# --------

# ----change function name----
print('# ----change function name----')
a = abs
print(a)
print(a(-1))
# --------

# ----def function----
print('# ----def function----')


def age_definer(age):
    if age >= 18:
        return 'adult'
    elif age >= 13:
        return 'teenage'
    else:
        return 'child'


for n in range(20):
    print('age:%d is a %s' % (n, age_definer(n)))
# --------

# ----空返回函数----
print('# ----空返回函数----')


def print_name(name):
    print('your name is %s' % name)
    return


print_name('a')
print_name(123)
print(print_name('name2'))

# --------


# ----函数多个返回值----
print('# ----函数多个返回值----')


def position_translator(x, y, translate):
    x += translate;
    y += translate;

    return x, y


x1 = 123
y1 = 234
t = 100

x2, y2 = position_translator(x1, y1, t)

print(x2)
print(y2)

print('P1(%d, %d) translate to P2(%d, %d)' % (x1, x2, x2, y2))

value = position_translator(4, 5, 7)
print(value)  # value is a tuple
print(position_translator(2, 3, 5))
print(position_translator(4, 3, 1))


# --------

# ----函数参数类型检查----
print('# ----函数参数类型检查----')


def age_definer2(age):
    if not isinstance(age, (int, float)):
        raise TypeError('参数类型错误')
    if age >= 18:
        return 'adult'
    elif age >= 13:
        return 'teenage'
    else:
        return 'child'

# print(age_definer2('a'))  # 错误!参数类型不正确，但是函数没有检查参数类型
# --------


# ----函数的参数定义----
print('# ----函数的参数定义----')


def power(x, pn=2):  # 默认参数2
    pv = 1
    for i in range(pn):
        pv *= x
    return pv


print(power(3, 2))
print(power(3))
print(power(3, 3))
# --------

# ----函数的可变参数----
print('# ----函数的可变参数----')


def sum(*numbers):
    ss = 0
    for ns in numbers:
        ss += ns
    return ss


print(sum(1, 2, 3, 4, 5))

nums1 = [1, 2, 3, 4, 5]

print(sum(nums1[0], nums1[1]))
print(sum(*nums1))  # 将list转化为可变参，方便调用

# --------

# ----函数的关键字参数（Key-Value可变参数)----
print('# ----函数的关键字参数（Key-Value可变参数)----')


def person(name, age, **kw):
    print('name:', name, "age:", age, "other:", kw)
    return


person('mr', 29)
person('mr', 29, city='abc')
person('mr', 29, city='abc', comp='pg')

info = {'city': 'abc', 'comp': 'pg', 'job': 'engineer'}
person('mr', 29, **info)  # 将info转化为可变参，方便调用

# --------

# ----参数组合----
print('# ----参数组合----')
print('# ----参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数----')


def func(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 4)
func(1, 2, 3, 4, 5)
func(1, 2, 3, 4, 5, 6, k1=7, k2=8)

args = {1, 2, 3, 4, 5, 6}
kws = {'k1': 7, 'k2': 8}
func(*args, **kws)  # 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# --------

# ----递归函数----
print('# ----递归函数----')

def fact(fn):
    if fn == 1:
        return 1
    else:
        return fn * fact(fn - 1)

print('1!=', fact(1))
print('2!=', fact(2))
print('5!=', fact(5))
print('10!=', fact(10))
# print('100!=', fact(1000))  # Stack over flow

# --------
