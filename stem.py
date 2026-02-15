"""
my_name=['abdullah' , 'elsaied' , 'gomma' ]
my_name.append( 'abdullah')
p=my_name.count('abdullah')
o=my_name.index('gomma')
my_name.insert(1,'capten')
my_name.pop(-1)
my_name.remove('abdullah')
my_name.sort()
my_name.reverse()
my_name.append(my_things)
list.insert(index.obj)
list.index(obj) 
list.extend()
list.count(obj)
list.append(obj)
my_things=['book' , 'pens' , 'bag' , 'paper']
print(my_name)
print(o)
"""


tup1=('age', 'salary' , 'game' , 'my car')
tup2=('I' , 'learn ' ,'in ' , 'delta' , 'univ')
print((tup1,tup2))
print(tup1 == tup2)
print(tup1 < tup2)
print(tup1 < tup2)
tup3=('5','6','7')
tup4=('1','2','3')
print(tup1 == tup2  == tup3 == tup4)
print(tup1 , tup2  , tup3 , tup4)
print(len(tup1 ) , len(tup2 ) , len(tup3 )  , len(tup4 )  )
print(max(tup1 ))
print(min(tup4))
list1=['car' , 'lab']
tup3=tuple(list1)
print(tup3)




dict1={ 'name':'abdullah' , 'age':19  , 'salary':15000}
dict2={'locate':'cairo' , 'job':'AI ENG'}
dict3={0:34567890 , 79:7689}
print(dict1 == dict2 == dict3)
pop=len(dict1)
print(pop)
str(dict3)
print(dict3)
print(type(7689))
if 'name' in dict1:
    print("yes ")
all_key=dict3.keys()
print(all_key)
all_values=dict1.values()
print(all_values)
all_items=dict1.items()
print(all_items)
print(dict1.clear())
new_dict=dict2.copy()
print(new_dict)

user = {"name": "Ali", "age": 25}
new_data = {"age": 26, "city": "Cairo"}
user.update(new_data)
print(user)
scores = {"momo": 90, "Sara": 95}
print(scores.get("Ahmed", 0)) 
print(user.pop("name"))
print(user)
print(user.popitem())
print(user)
for x in dict2:
    print(x)
for x in user:
    print(user[x])
for x in dict1.values():
    print(x)
"""
num=int(input("enter the firts number"))
if num%2==0:
   print("number is even")

age=0
while(age<100):
    print("the age is :", age)
    age=age+1
print("good bye!")
"""

ages=[6 , 1 , 60 ]
for num in ages:
    if num == 6:
        print("he is a boy , his age is %d  " %(num))
    elif num == 60:
        print("he is a oldman , his age is %d " %(num))
    else:
        print("he is a baby , his age is %d " %(num))

str1="python"
for i in str1:
    print(i)

x=[2,3,4,5,6,7,8]
for y in x:
    if y==5:
        continue
    print(y)

x=[2,3,4,5,6,7,8]
for y in x:
    if y==5:
        break
    print(y)
