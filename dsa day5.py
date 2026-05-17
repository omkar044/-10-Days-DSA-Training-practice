# import sys
# class Queue:
#     def __init__(self):
#         self.queue=[]
#         self.rear=-1
#         self.front=0
#         self.CAPACITY=5

#     def isFull(self):
#         if self.rear==self.CAPACITY-1:
#             return True
#         else:
#             return False

#     def insert(self,ele):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.rear = self.rear + 1
#             self.queue.append(ele)
#             print(ele, "is inserted")
        

#     def traverse(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Queue elements are:")
#             for i in self.queue:
#                 print(i)
      

#     def isEmpty(self):
#         if self.rear==-1:
#             return True
#         else:
#             return False

#     def delete(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             ele = self.queue.pop(0)
#             self.rear = self.rear - 1

#             if len(self.queue) == 0:
#                 self.rear = -1

#             return ele
            
        
        
    
#     def peek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Front element is:", self.queue[0])
     

# if __name__ == '__main__':
#     obj=Queue()
#     while True:
#         print("1. insert")
#         print("2. delete")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         ch=int(input("select any choice:"))
#         if ch==1:
#             ele=int(input("Enter data: "))
#             obj.insert(ele)
#         elif ch==2:
#             obj.delete()
#         elif ch==3:
#             obj.peek()
#         elif ch==4:
#             obj.traverse()
#         elif ch==0:
#             sys.exit(0)


#--------------------------------Reverse the Queue using Stack--------------------------------------------------------
# import sys


# class Stack:

#     def __init__(self):
#         self.stack = []
#         self.top = -1
#         self.CAPACITY = 5

#     def isFull(self):
#         if self.top == self.CAPACITY - 1:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False

#     def push(self, ele):
#         if self.isFull():
#             print("Stack is Full")
#         else:
#             self.top = self.top + 1
#             self.stack.append(ele)

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             ele = self.stack.pop()
#             self.top = self.top - 1
#             return ele



# class Queue:

#     def __init__(self):
#         self.queue = []
#         self.rear = -1
#         self.front = 0
#         self.CAPACITY = 5

#     def isFull(self):
#         if self.rear == self.CAPACITY - 1:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if self.rear == -1:
#             return True
#         else:
#             return False

#     def insert(self, ele):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.rear = self.rear + 1
#             self.queue.append(ele)
#             print(ele, "is inserted")

#     def delete(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             ele = self.queue.pop(0)
#             self.rear = self.rear - 1

#             if len(self.queue) == 0:
#                 self.rear = -1

#             return ele

#     def traverse(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Queue Elements:")
#             for i in self.queue:
#                 print(i)



# if __name__ == '__main__':
#     q = Queue()
#     s = Stack()

    
#     n = int(input("Enter number of elements: "))

#     for i in range(n):
#         ele = int(input("Enter element: "))
#         q.insert(ele)

#     print("\nOriginal Queue:")
#     q.traverse()

#     for i in range(n):
#         ele=q.delete()
#         s.push(ele)

#     for i in range(n):
#         ele=s.pop()
#         q.insert(ele)
  

#     print("\nReversed Queue:")
#     q.traverse()


#--------------------------------------Array and Stack ----------------------------------------------------




#---------------insert key element in array---------------------------
# arr = [10, 20, 30, 40, 50]

# ele = 99
# loc = 3


# arr.append(0)

# for i in range(len(arr)-1, loc, -1):
#     arr[i] = arr[i-1]


# arr[loc] = ele

# print("Array after insertion:")

# for i in arr:
#     print(i, end=" ")


#---------------------delete key element from array------------
# arr = [10, 20, 30, 40, 50]

# loc = 3  

# for i in range(loc, len(arr)-1):
#     arr[i] = arr[i+1]

# arr.pop()
# print("Array after deletion:")

# for i in arr:
#     print(i, end=" ")
#----------------array rotation------------------
# arr = [1, 2, 3, 4, 5]
# k= 2

# for j in range(k):
#     temp = arr[len(arr)-1]

#     for i in range(len(arr)-1, 0, -1):
#         arr[i] = arr[i-1]
#     arr[0] = temp

# print("Array after rotation:")

# for i in arr:
#     print(i, end=" ")

#----------------intersection of two array--------------
# arr1 = [1, 2, 2, 1]
# arr2 = [2, 2,]

# intersection = []

# for i in range(len(arr1)):
#     for j in range(len(arr2)):

#         if arr1[i] == arr2[j]:

#             if arr1[i] not in intersection:
#                 intersection.append(arr1[i])

# for i in intersection:
#     print(i, end=" ")

#-----------------Rearrange alternate positive and negative element---------
# 
# arr = [5, -2, 1, -6, 3, -4]

# pos = []
# neg = []


# for i in arr:

#     if i >= 0:
#         pos.append(i)

#     else:
#         neg.append(i)


# for i in range(len(pos)):
#     for j in range(i + 1, len(pos)):

#         if pos[i] > pos[j]:
#             temp = pos[i]
#             pos[i] = pos[j]
#             pos[j] = temp


# for i in range(len(neg)):
#     for j in range(i + 1, len(neg)):

#         if neg[i] < neg[j]:
#             temp = neg[i]
#             neg[i] = neg[j]
#             neg[j] = temp


# for i in range(min(len(pos), len(neg))):

#     print(pos[i], end=",")

#     if i == len(neg) - 1:
#         print(neg[i], end="")
#     else:
#         print(neg[i], end=",")


#--------------------------Reverse a string ------------------------------------
# string = "omkar"

# reverse = ""

# for i in range(len(string)-1, -1, -1):
#     reverse = reverse + string[i]
# print( reverse)
#---------------------check for valid palandromic string-----------------------
# s = "A man, a plan, a canal: Panama"
# new = ""
# for i in s:

#     if i.isalnum():
#         new = new + i.lower()
# left = 0
# right = len(new) - 1
# flag = True

# while left < right:
#     if new[left] != new[right]:
#         flag = False
#         break

#     left += 1
#     right -= 1

# if flag:
#     print("Valid Palindrome")
# else:
#     print("Not Palindrome")

#---------------------------check for  anagrams----------------------
# str1 = "listen"
# str2 = "silent"

# str1 = str1.lower()
# str2 = str2.lower()

# if len(str1) != len(str2):
#     print("Not Anagram")

# else:
#     flag = True

#     for i in str1:
#         if str1.count(i) != str2.count(i):
#             flag = False
#             break

#     if flag:
#         print("Anagrams")
#     else:
#         print("Not Anagram")