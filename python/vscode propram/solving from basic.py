# age=20
# print(age)

# age1 = float(age)
# print(age1)

# s="10"
# print(type(s))

# print(int(s)+age)


# p=400

# print(s,p)


# a, b=10,12
# print(a+ b)



# integer = input("Enter the Age : ")
# print(integer)


# boy_name = input("Enter the boy name")
# girl_name = input("Enter the girl name")
# print("'"+boy_name+"'" + "'Loves'" + girl_name)



# Girlage= input('Enter the age : ')
# Boyage= input('Enter the age : ')
# age_Difference = int(Girlage)- int(Boyage)
# print(f"Age Difference { age_Difference}")

# '''Absolute vale is used for the modulues type
# Where "abs" = Absolute value   
# '''
# age_Difference = abs(int(Girlage)- int(Boyage))



# manoj= str(input("Enter the name : "))
# print(manoj)

# def add_Numbers(x,y,z):
#     return x+y+z



# q= int(input("Enter the Number to add : " ))
# w= int(input("Enter the Number to add : " ))
# e= int(input("Enter the Number to add : " ))
# print(add_Numbers(q,w,e))


'''String manipulation
String manupulation means anlyzing modifying'''

# message = 'Hello!..'
# print(message*3)

# '''Concatination'''
# a='123'
# b='123'
# print(f"{a} {b} ")

# name="manoj"
# print(name[0:])

# message = "Hello"
# print(len(message))
# print(message.upper())
# print(message.replace("Hello" , "123"))


# name = "manoj"
# print(name[:2])

# mylist = [1,2,3,4]
# mystring="python"
# print(mystring.index("p"))
# print(3 in mylist)
# print(5 not in mylist)
# print("p" in mystring)



# name = "manoj"
# character = "a"
# name1= True
# if character in name:
#     print(name1)
# else:
#     name1=False
#     print(name1)


# import math

# def AddNumber(a,b):
#     return abs(a-b)

# result = AddNumber(2,4)
# print(result)


# name = "manoj"
# print(name[1:2])

# def ispalindrome(s):
#     result = s[::-1]
#     if s==result:
#         return True
#     else:
#         return False
    

# print(ispalindrome("-121"))


# def isPalindrome(x):
#         result =x[::-1]
#         if result ==x:
#             return True
#         else:
#             return False


# print(isPalindrome("Hello"))


# def reversed(x):
#     result = x[::-1]
#     if result==x:
#         return True
#     else:
#         return False

# print(reversed("Hello"))

'''
a list is a collection of items that are ordered , mutable(changable)
and allow duplicate element it hold the differnet types of the data 
such as string integer
'''
'''Diference1'''
# items = ["bru", "sugar","milk"]
# print(items.pop())

'''Difference2'''
'''Diference between Diference1 and Diference2 this two is'''
# items = ["bru", "sugar", "milk"]
# items.pop()  # Removes the last item ('milk')
# print(items)  # Prints the remaining items ['bru', 'sugar']


'''The pop() method modifies the list by removing an element.
The returned value ("milk") is what gets printed because you 
explicitly use print(items.pop()).
If You Want to Print the Remaining Items:
After calling pop(), the list will be modified, 
so you need to print the updated list instead of the 
value returned by pop().

'''


# items=[1,2,3 , "Hello","man", ["Hello","position"]]
# print(items[5])
# items.pop()

# print(items)

'''This all are modifing the list'''

'''pop is used to remove the element '''
# items=[1,2,3 , "Hello","man", ["Hello","position"]]
# print(items.pop())  #This will remove the last element
# print(items.pop(1)) # this will remove the particular postion of that index

# items = ["bru", "sugar" , "Milk"]
# items.remove("bru")
# print(items)
'''Remove method is used to remove the paricular item from the list'''

'''Insert method is used to add the new item on the postion we need '''
# items = ["bru", "sugar" , "Milk"]
# items.insert(2,5)
# print(items)


'''Inserting at an index beyond the current length of the 
list appends the element at the end:
it will add at the last'''
# lst = [1, 2, 3]
# lst.insert(10, 4)
# print(lst)  # Output: [1, 2, 3, 4]

'''Negative indices count backward from the end:'''
# lst = [1, 2, 3]
# lst.insert(-1, "middle")
# print(lst)  # Output: [1, 2, 'middle', 3]

# lst = [1, 2, 3]
# lst.insert(1, ["middle","hello", 1])
# print(lst)  # Output: [1, 2, 'middle', 3]

'''Append is uded to add any item for the list in the lat position'''
# list = [1,2,3]
# new_list = list + [8]
# print(new_list)

# my_list = [1, "apple", 3.14]
# my_list.append(True)  # Adding a boolean
# my_list.append([5, 6])  # Adding another list
# my_list.append({"a": 1})  # Adding a dictionary
# print(my_list)
# # Output: [1, 'apple', 3.14, True, [5, 6], {'a': 1}]

'''To clear the entire list then it will be empty  list'''
# list=[1,2,3]
# list.clear()
# print(list)
# print(list[1])

'''To replace the the items of the list'''

'''Slicing'''
# l=[100,200,300,400]
# l[0:4]
# print(l)

'''Changing the Value'''

# list = [1,2,3,4,5]
# list[0] = 5
# print(list)


'''Reverse and sorted'''

# list = [2,5,8,6,7,9,4,2]
# newlist = sorted(set(list))
# print(newlist)


# list = [2,5,8,6,7,9,4,2]
# list.sort()
# print(list)
''' output [2, 2, 4, 5, 6, 7, 8, 9]  in this the duplicate value will 
be present
'''

'''Reverse'''

list = ["manoj", "Kushal",1 ,2 ,3 ]
list.reverse()
print(list)
