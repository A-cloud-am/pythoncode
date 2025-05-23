#map data type=dictionary=key value pair,mutable(original data changeable),
#order,duplicate key doesnot allowed 

# a=dict()
# print(type(a))
#syntax:
# dict_name={
#     'key':"value",
#     'key1':"value2"}
# example
a={
    'name':"amisha",
    "age":45
}
print(a)
print(len(a))
#accessing values of dictionary
#two methods
#indexing,get()
#indexing
# print(a['address'])
#get()
print(a.get('address',"data not found"))

print(a.keys())
print(a.values())
print(a.items())

#create a dictionary that takes students marks in different subjects
#  and print students average percentage (total value/len)  
# sum()

grade={
    'social':89,
    'english':78,
    'math':99,
    'science':56,
    'nepali':90
}
x=len(grade)
a=sum(grade.values())
avg=a/x
print(f"your average marks is {avg}")

#formatted string(f)
# a="welocme"
# # print("siplaya",a)

# print(f" {a} greetings ")

