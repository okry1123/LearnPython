__author__ = 'apple'
# ----dict----
print('----dict----')
dict1 = {'mr': 29, 'lq': 29, 'fyb': 54}
print(dict1)
print(dict1['lq'])

dict1['mpl'] = 58
print(dict1)

dict1['lq'] = 30
print(dict1)

if 'olly' in dict1:
    print(True)
else:
    print(False)
print(dict1.get('lq'))
print(dict1.get('olly'))  # Get一个没有的元素不会报错

dict1[2] = 3

print(dict1)  # 混合类型dict

# --------

# ----set----
print('----set----')
set1 = set([1, 2, 3, 5, 5, 6, 6, 6, 6,])
print(set1)

set2 = set([1, 3, 7, 9])
print(set2)

set1.remove(1)
print(set1)

set2.add(4)
print(set2)

print(set1 & set2)
print(set1 | set2)

set2.remove(3)
print(set1 & set2)

# --------
