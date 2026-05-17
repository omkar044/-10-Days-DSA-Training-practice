# def bubbleSort(arr):
 
#  for i in range(len(arr)-1):
#   for j in range(len(arr)-1-i):
#    if arr[j]>arr[j+1]:
#     temp=arr[j]
#     arr[j]=arr[j+1]
#     arr[j+1]=temp
 
# if __name__=='__main__':
#  arr=[6,23,3,4,1,56,33]
#  bubbleSort(arr)
#  print(arr)
#  print(*arr)

# def selectionSort(arr):
 
#  for i in range(len(arr)):
#   min=arr[i]  
#   for j in range(i+1,len(arr)-1):
#    if min<arr[j]:
#     min=arr[j]
#     loc =j
  
#   temp=arr[i]
#   arr[i]=arr[loc]
#   arr[loc]=temp
  

# if __name__=='__main__':
#  arr=[6,23,3,4,1,56,33]
#  selectionSort(arr)
#  print(arr)
#  print(*arr)

#Insertion sort is much more efficient than Bubble and Selection sort.
# def insertionSort(arr):
#     for i in range(1,len(arr)):
#        temp=arr[i]
#        j=i-1
#        while j>=0 and arr[j]>temp:
#            arr[j+1]=arr[j]
#            j=j-1
#     arr[j+1]=temp

# if __name__=='__main__':
#     arr=[6,4,89,23,9,1,22,3]
#     insertionSort(arr)
#     print(arr)
#     print(*arr)

# Class:
# Class is the logical representation of things. It is like a blueprint or templet for the object

# Object: It is physical representation of the class and physical repesentation of things.

# class Student:                      #Class creation.
#     def show(self):                     #Function. In python first parameter in function is 'self'
#         print("I am a show") 


# #In C++: Object Creation:
# # Student s;              #static object
# # Student *s=new Student();       #Dynamic Object           

# # In java
# # Student s=new Student();

# #In Python
# s=Student();
# s.show();

# class Student:
#     def __init__(self):
#         print("default constructor ")

#     def show(self):
#         print("i am in show")

# s=Student();
# s.show();

# class Student:
#     def __init__(self):
#         print("default constructor ")

#     def show(self,a):
#         print(a)
#     def show(self,a,b):
#         print(a,b)

# s=Student();
# s.show();

