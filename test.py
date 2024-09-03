# shift = (1<<2)
# print(shift)
# def sample(*argv):
#     for arg in argv:
#         print(arg)
# sample("Hi","Hello","Bro","what")

# def sample_1(**kwargs):
#     for key,value in kwargs.items():
#         print("%s ->  %s"%(key,value))
# sample_1(key1 = 'value1',key2 = 'value2',key3 = 'value3')

# args = ('a','b','c')
# t = ['a','b','c']
# def fun1(arg1,arg2,arg3):
#     print(arg1,arg2,arg3)
# fun1(*args)
# fun1(*t)
# z = {'key1':'value1','key2':'value2','key3':'value3'}
# print(z)
# def fun2(key1,key2,key3):
#     print(key1,key2,key3)
# fun2(**z)
# import time
# import math
# def calculate__time(func):
#     def inner1(*args,**kwargs):
#         st = time.time()
#         func(*args,**kwargs)
#         ed = time.time()
#         print("Total time taken in  : ",func.__name__,ed-st)
#     return inner1

# @calculate__time
# def fac(num):
#     time.sleep(2)
#     print(math.factorial(num))

# fac(10)

# chaining decorators

# def dec1(func):
#     def inner1(x):
#         return func(x) * func(x)   
#     return inner1
# def dec2(func):
#     def inner2(x):
#         return 2 * func(x)
#     return inner2


# @dec2
# @dec1
# def change(num):
#     return num

# print(change(10))

# lst = []
# n = int(input("Enter the length : "))
# for i in range(n):
#     lst.append(int(input("Enter Element : ")))

# print(lst)

# lst = [1,12,3,4,5]
# print(lst)
# # lst.remove(2)
# print(len(lst))
# print(max(lst))
# print(min(lst))

tup = "ji",12,"Hello","ho"
print(tup)

# print(type(tup))
# print(id(tup))
# lst = [1,2,3,4]
# lst1 = [5,6,7,9]
# print(id(lst[0]),id(lst1[0]))
# print(id(lst[1]))
# print(id(lst[2]))
# print(id(lst[3]))

# try:
#     tup[0] = 1
# except Exception as error:
#     print(error)
#     # print("Tuple cannnot be modified")

lst = [1,2,3]
# lst.clear()
# print(lst)
class list1:
    def __init__(self,lst):
        self.lst = lst
    def length(self):
        return len(lst)

l1 = list1(lst)

print(l1.length())

part_square = [i**2 if i%2==0 else i+1 for i in range(10,21)]
print(part_square)


# del tup