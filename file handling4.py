#seek() method
'''a=open('h.txt','wb+')
print(a.tell())
a.seek(10,0)
a.seek(-2,1)
print(a.tell())
a.close()'''

a=open('h.txt','rb+')
print(a.tell())
data=a.read(3)
print(a.tell())
print(data)
data=a.read(3)
print(data)
print(a.tell())
a.close()

'''
OUTPUT
0
3
b'cod'
b'ing'
6
'''
