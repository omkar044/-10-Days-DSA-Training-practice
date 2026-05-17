#----------------------------Function---------------------------------------------------------- 

# def add(a,b):
#     a =int (input ("enter the a: "))
#     b =int (input ("enter the b: "))
#     res = a + b
#     print("addition is ",res)




#  if __name__=='__main__':
#     a =int (input ("enter the a: "))
#     b =int (input ("enter the b: "))
#     add(a,b)


# def add(a,b):
#  res=a+b
#  return res
#  if __name__=='__main__':
#     a =int (input ("enter the a: "))
#     b =int (input ("enter the b: "))
#     r=add(a,b)
#     print("addition is ",r)

# def add(a,b):
#   res1=a+b
#   res2=a-b
#   res3=a*b
#   return res1,res2,res3

#   if __name__=='__main__':
#      a =int (input ("enter the a: "))
#      b =int (input ("enter the b: "))
#      r1,r2,r3=add(a,b)
#      print("addition is ",r1)
#      print("substraction is ",r2)
#      print("multiplication is ",r3)


#------------------------------------------------Linear search-----------------------------------------------------
# def linear_search(n,arr,target):
#     flag=False
#     for i in range(n):
#         if target!=arr[i]:
#             pass
#         else:
#             flag=True
#             loc=i
#     if flag==True:
#         print("search is sucessfull and present at",loc)
#     else:
#          print("search is unsucessfull")  


# if __name__=='__main__':
#     n=int(input("Enter Size:"))
#     arr=[]
#     for i in range(n):
#         arr.append(int(input()))
#     target=int(input("Enter num which is to be search:"))
#     linear_search(n,arr,target)

# def linear_search(n,arr,target):
#     flag=False
#     low=0
#     high=n-1
#     loc=-1
#     while low<=high:
#         mid=(low+high)//2
#         if(target==arr[mid]):
#             flag=True
#             loc=mid
#             break
#         elif target<arr[mid]:
#             high=mid-1
#         elif target>arr[mid]:
#             high=mid+1
#         if flag:
#           print("Element found at index:",loc)
#         else:
#            print("Element not found")


    


# if __name__=='__main__':
#     n=int(input("Enter Size:"))
#     arr=[]
#     for i in range(n):
#         arr.append(int(input()))
#     target=int(input("Enter num which is to be search:"))
#     linear_search(n,arr,target)