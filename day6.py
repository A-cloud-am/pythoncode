#mutable(original data changeable)

# a['name']="hari"
# print(a)
# a['subject']='engineer'
# print(a)

# print(len(a))

# #order:(indexig)(single pair adding)
# a['email']="hari@gmail.com"
# a['address']="ktm"
# print(a)


#adding multiple pair
#update

a={
    'name':"komal",
    'subject':"science",
    
}
b={
    'age':67,
    'email':"hari@gmail.com",
    'address':"butwal"
}
a.update(b)
print(a)

# #deleting methods
# del a['email']
# del a['age']
# print(a)

# #pop()
# a.pop('address')
# print(a)

#popitem()
a.popitem()
print(a)

#nested

grade={
    'student':{
        'name':"sita",
        'age':78
    },
    'student2':{
        'name':'rita',
        'age':45
    }
}

print(grade['student']['name'])
print(grade['student2']['name'])

grade['student']['name']='nita'
print(grade)


#binary data type=memory management,it handles binary file,image,audio,video
#two types
#1)bytes  2)bytearray

#bytes=it generates sequence of numbers generate,range(0,256),immutable(original data not chnageable)
a=bytes([1,2,3,4,5,7,8])
print(type(a))
print(a)
print(a[::2])
# a[0]=6
# print(a)

#bytearray=it genertaes sequence of numbers,range(0,256),mutable(original data changeable)
a=bytearray([1,2,3,4,5,8,100,255])
print(type(a))
print(a)
print(a[:3])
a[0]=7
print(a)


#boolean=True False   True=1  False=0
a=True
print(type(a))


#None data type=absenece of value
a=None
print(a)
print(type(a))


