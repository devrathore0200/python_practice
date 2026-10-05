# 1-check prime number 
# n=int(input("enter the value :"))
# count =0
# for i in range (1,n):
#     if n%i ==0 :
#         count +=1
# if count == 2:
#     print("value is prime number:",i)
# else:
#     print("value is not prime number:",i)
# check even number
# 2-n = int(input("entert the vlue :"))
# even_sum = 0
# odd_sum  = 0
# for i in range (1,n+1):
#     if i % 2 == 0:
#         print("even number :",i)
#         even_sum += i
#     else:
#         print("odd number :",i)
#         odd_sum +=  i
# print("total even sum is :",even_sum)
# print("total odd sum is :",odd_sum)
# programe make three number in acending order
num1 =int(input("enter the value:"))
num2 =int(input("enter the value:"))
num3 =int(input("enter the value:"))
if num1>=num2 and num1>=num3:
    if num2>=num3:
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)
elif num2>=num1 and num2>=num3:
    if num1>=num3:
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)
else:
    if num1>=num2:
            print(num3,num1,num2)
    else:
            print(num3,num2,num1)

