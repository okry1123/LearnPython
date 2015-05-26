__author__ = 'apple'
# ----list测试----
family = ['MR', 'LQ', 'Olly']
family.append(6000)# 混合类型可以
family.insert(1, 'father')
print(family)
print('length:' + str(len(family)))
print('child:' + family[2])

family2 = ['Father', 'Mather', ['MR', 'LQ']]
print(family2)
print(family2[-1])
print(family2.pop())
print(family2)
# ---------------

# ----tuple:不可变List----
solidlist = (1, 2, 3)
# solidlist[0] = 4 # This can is forbidden
print(solidlist)
# ---------------
