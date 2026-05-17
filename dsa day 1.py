# num =int(input("Enter no"))
# res =num%10;
# print(res);

# num =int(input("Enter no"))
# n1 = num%10;
# n2 = num//10;
# res = n1+n2;
# print(res);

# num =int(input("Enter no"))
# n1 = num%10
# num = num//10
# n2 = num%10
# num =num//10
# n3 = num%10

# res = n1 +n2 +n3
# print(res)

# num =int(input("Enter no"))
# n1 = num%10
# num = num//10
# n2 = num%10
# num =num//10
# n3 = num%10
# num =num//10
# n4 = num%10
# num =num//10
# n5 = num%10

# res = n1 +n2 +n3 +n4 +n5
# print(res)

#  num =int(input("Enter no"))
#  n1 = num%10
#  num = num//10
#  n2 = num%10
#  num =num//10
#  n3 = num%10
#  rev = n1*100 +n2*10 +n3*1
#  print(rev)

# num =int(input("Enter num"))
# rev = 0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num =num//10
# print (rev)

# num =int(input("Enter num"))
# count = 0

# while (num>0):
#     num =num//10
#     count+=1

#     print (count)

# num =int(input("Enter num"))
# sum = 0
# count=0
# while num>0:
#     n1 =num%10
#     sum+=n1
#     num = num//10
#     count+=1
#     print(sum)

# num =int(input("Enter num"))
# fact =1
# while num>0:
#  fact =fact*num
#  num=num-1
#  print (fact)

# num =int(input("Enter num"))
# sum=0
# save=num

# count=0
# while num>0:
#     num=num//10
#     count+=1



# while save>0:
#     rem=save%10
#     sum=sum+(rem**count)
#     num=num//10

# if (sum==save):
#     print("num is armstrong")
# else:
#     print("num is not armstrong")


# num =int(input("Enter num"))

# fact=1
# sum=0
# save=num

# while num>0:
#     rem=num%10
    
#     fact=1
#     while rem>0:
#         fact=fact*rem
#         rem=rem-1
#     sum=sum+fact
#     num=num//10
#     print(sum)
# if save==sum:
#     print("value is peterson")
# else:
#     print("value is not peterson")

# n1 = 10
# n2 = 20
# n3 = 30
# max= n1
# if max<n2:
#     max=n2
# if max<n3:
#     max=n3
# print(max)

#-----------if else-----------
# num = 5
# if num%2 ==0:
#     print(num,"is even")
# else
#     print(num,"is odd")


#------------ladder elif--------
# per=75
# if per>=40 and per<=60:
#     print("Take add in abc clg")
# elif per>=61 and per<=80:
#     print("Take add in xyz clg")
# elif per>=81 and per<=100:
#     print("Take add in  clg")

#----------------for-------------

# for i in range (1,11):
#     print(i)

# arr =[1,2,3,4,5,5]   
# for i in range(len(arr)):
#      print(arr[i])





# ls =[]
# print(type(ls))
# ls=list()
# ls=[1,2,3,34,77,88]
# print(type(ls))


# arr=[1,2,3,34,77,88]
# print(type(arr))

# for i in range(len(arr)):
#     print(arr[i])

#--------------Slicing-------

# arr=[11,22,33,44,55,66,77]
# print(arr[4])
# print(arr[-1])
# print(arr[1:5])
# print(arr[4:6])
# print(arr[:6])
# print(arr[4:])
# print(arr[:]) 
# print(arr[::1])
# print(arr[::2])       
# print(arr[::3])
# print(arr[::-1])

# arr=[7,6,9,4,5]
# max =arr[0]
# min =arr[0]
# for i in range(1,len(arr)):
#     if max<arr[i]:
#          max=arr[i]
         
#     if min>arr[i]:
#         min=arr[i]
         
# print("maximumn",max)
# print("minimumn",min)


#-----------Remove Duplicate value---------
arr=[3,1,2,3,1,4]
ans = []

for item in arr:
    if item not in ans:
        ans.append(item)

print(ans)