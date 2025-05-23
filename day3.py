#sequence data type=list
#list=collection of data,data is seperated by comma,data format or data structure
#mutable(original data chanegable),it allow duplicate value,order
# a=12
# b=45.89
# c="hello"
# a=[12,34.67,"hello","world",67]
# print(type(a))
# print(a)
# print(len(a))

# #indexing
# #syntax:variable_name[index]
# print(a[-3])
# print(a[2][0])
# print(a[2][-1])


#slicing:
#syntax:variable_name[start:end:step]
# print(a[0:3:1])
# print(a[-2:])
# print(a[2][0:3:1])
# print(a[-2][-5:])

# a=[12,12,12,"hel lo","hello","world","world",56,56,56,56]
# print(a)
# print(len(a))


# a[-2]=90
# print(a)

#list inbuilts methods=precoded or predefined
#adding methods
#order

#1)append()=adding data in list single data adding
# a.append(23)
# print(a)
# print(a[-1][0])
#2)adding multiple data
# extend()
# a.extend([56,"rita","amisha",78])
# print(a)

#adding data randomly in any index
#insert()
# a.insert(2,["hello",34,89.56])
# print(a)

#deleting methods
#1)pop()  #LIFO
a=[12,34.78,"hello","tina",67,"hari"]
a.pop(1)
print(a)
# #remove()=it removes particular data
# a.remove("tina")
# print(a)

#clear()=it removes all content of listbut returns empty list
# a.clear()
# print(a)

# del(keyword)
# # del a
# # print(a)
# # print()
# # type()
# # len()

# #sorting methods
# #sort()=method  sorted()=inbuilt function

# a=[5,7,1,2,8,9,3]
# a.sort(reverse=True) #ascending order reverse=True(descending)
# print(a)


# a=[5,7,1,2,8,9,3]
# b=sorted(a,reverse=True)
# print(b)


# var=["apple","orangesss","pear","cow"]
# var.sort(key=len,reverse=True)
# print(var)

# b=sorted(var,key=len,reverse=True)
# print(b)

