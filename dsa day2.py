# arr =[11,22,33]
# print (arr)
# for i in range(len(arr)):
#     print(arr[i])

# arr =[[1,2,3],[4,5,6],[7,8,9]]
# print(arr)
# for x in range(len(arr)):
#     print(arr[x])

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j],end="  ")

# s = set()
# print(s)  
# print(type(s))  

# g = {1,2,3,4,5,3,2,4,3,2,4,4}
# print(g)  

# arr =[1,2,3,4,5,3,2,4,3,2,4,4]
# s=set(arr)
# arr = list(s)
# print(arr)

# n=int(input("Enter Size:"))
# print("Enter list element:")
# arr=[]
# for i in range(n):
#     ele =int(input("Enter element :"))
#     arr.append(ele)
# for i in range(len(arr)):
#     print(arr[i],end=" ")  

#sum of list
# n = int(input("Enter size: "))

# arr = []

# print("Enter elements:")
# for i in range(n):
#     num = int(input())
#     arr.append(num)

# sum = 0

# for i in range(len(arr)):
#     sum = sum + arr[i]

# print("Sum:", sum)

#add of even no

# n = int(input("Enter size: "))

# arr = []

# print("Enter elements:")
# for i in range(n):
#     num = int(input())
#     arr.append(num)

# sum = 0
# for i in range(len(arr)):
#      if arr[i]%2==0:
#          sum = sum + arr[i]
# print("Sum:", sum)

#no of even and odd

# n = int(input("Enter size: "))

# arr = []
# even=0
# odd=0
# e1=0
# o1=0
# print("Enter elements:")
# for i in range(n):
#     num = int(input())
#     arr.append(num)


# for i in range(len(arr)):
#      if arr[i]%2==0:
#       even=+1
#       e1count=+1
#       print("even",even,e1)  
#      else:
#         odd=+1
#         o1count=+1
#         print("odd",odd,o1)
      
#important question
# num =int(input("enter the number: "))
# sum=0
# mul=0
# num1=num%100
# num=num//100
# sum=num+num1
# mul=sum*sum
# print(num1,"+",num,"=",sum)
# print(sum,"*",sum,"=",mul)



# num =int(input("enter the number: "))
# num1=num%100
# num2=num//100
# sum=num1+num2

# mul=sum*sum
# if mul==num:
#     print("tech number")
# else:
#     print("non tech number")

# print(num1,"+",num,"=",sum)
# print(sum,"*",sum,"=",mul)


#for any digit
# no=int(input("Enter number:"))
# count=0
# save=no
# while no>0:
#     no=no//10
#     count=count+1
# no=save
# if count%2==0:
#     count=count/2
#     num1=save%10**count
#     num2=save//10**count
#     sum=num1+num2
#     mul=sum*sum
#     print(" tech number")
#     # print(num1,"+",no,"=",sum)
#     # print(sum,"*",sum,"=",mul)

# else: 
#     print("no tech number")


# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print() 

# n=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(n,end="\t")
#         n=n+1
#     print()


# n=65
#for i in range(1,5):
#     for j in range(1,5):
#         print(chr(n),end="\t")
#         n=n+1
#     print()

# for i in range(1,5):
#      for j in range(1,i+1):
#          print(i,end="\t")
#      print()

# for i in range(4,0,-1):
#      for j in range(1,i+1):
#          print("*",end="\t")
#      print()

# sp=0
# for i in range(4,0,-1):
#       for x in range(sp):
#            print(" ",end="")
#       for j in range(1,i+1):
#           print("*",end="")
#       print()
#       sp=sp+1


#------------------------------STRING-------------------------------------------------------------

# s="Learning Python is very easy from Ashish sir"
# print(s.find("Python"))
# print(s.find("java"))
# print(s.find("r"))
# print(s.rfind("r"))

# s="abcabcabcabcadda"
# print(s.count('a'))
# print(s.count('ab'))
# print(s.count('a',3,10))

# s="Learning Python is very difficult from Ashish sir"
# s1=s.replace("difficult","easy")
# print(s1)
 

# s="Learning Python is very difficult from Ashish Sir"
# ls=s.split()
# print(ls)
# print(len(ls))


# s="22-03-2002"
# ls=s.split("-")
# print(ls)

# s="www.ashish.com"
# ls=s.split(".")
# print(ls)

# l=['Nagpur','pune','Mumbai','Delhi']
# s=' '.join(l)
# print(s)

# s="Learning python is very easy from ashish sir"
# l=s.split()
# l=l[::-1]
# print(l)
# s=" ".join(l)
# print(s)

# s="Learning python is very easy from ashish sir"
# l=s.split()
# s=s[::-1]
# print(s)

# str ="ABCDBBCDABBBCCCDDEEEF"
# ans= ""
# for i in str:
#     if i not in ans:
#         ans+=i


# d={}
# d[100]="ashish"
# d[200]="omkar"
# d[300]="tanmay"
# print(d)

rec={}
n=int(input("Enter num of student:"))
for i in range(n):
    name=input("Enter name:" )
    per=float(input("Enter prec:"))
    rec[name]=per
print(rec)
for x in rec:
    print(x,"\t",rec[x])
   