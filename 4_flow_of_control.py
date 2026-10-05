#Intervie Task 1:
#even and odd number sum and list 
even_list = []
odd_list = []
even_sum =0
odd_sum =0
try:
    num = int(input("enter the value :"))
    for i in range(1,num+1):
        if i % 2 == 0:
            print("value is even number :",i)
            even_list.append(i)
            even_sum += i
        else:
            print("value is odd number :",i)
            odd_list.append(i)
            odd_sum += i
except ValueError:
    print("please enter the valid number")
print("total even sum is :",even_sum)
print("total odd sum is :",odd_sum)
print("even number list is :",even_list)
print("odd number list is :",odd_list)
#Intervie Task 2:
#Write a Python program that:
# Prompts the warehouse manager to enter the current stock count (as integers) for Hub A, Hub B, and Hub C.
# Handles invalid inputs (e.g., text instead of numbers) gracefully using exception handling.
# Compares the three counts and prints:
# The name of the hub with the largest stock and its quantity.
# If two or all three hubs tie for the highest stock, reports the tie clearly.
while True:
    try:
        hub_A=num=int(input("enter the value of hub A:")) 
        hub_B=num=int(input("enter the value of hub B:")) 
        hub_C=num=int(input("enter the value of hub C:")) 
        if hub_A==hub_B==hub_C:
            print("There is a tie for the largest stock b/w hub A, hub B and hub C")
            break
        elif hub_A==hub_B :
            print("There is a tie for the largest stock b/w hub A and hub B")
            break
        elif hub_B==hub_C :
            print("There is a tie for the largest stock b/w hub B and hub C")
            break
        elif hub_A==hub_C:
            print("There is a tie for the largest stock b/w hub A and hub C")
            break
        if hub_A>=hub_B and hub_A>=hub_C:
            print("hub A is the largest stock and quantity is :",hub_A)
        elif hub_B>=hub_A and hub_B>=hub_C:
            print("hub B is the largest stock and quantity is :",hub_B)
        else:
            print("hub C is the largest stock and quantity is :",hub_C)
    except ValueError:
        print("please enter the valid number")
#task 3:
sum1 = 0
sum2 = 0
num1 = int(input("enter the value of num1:"))
num2 = int(input("enter the value of num2:"))
num3 = int(input("enter the value of num3:"))
sum1 = num1 +num2+ num3
if num1!=num2 and num1!=num3:
    sum2 += num1
if num2!=num3 and num2!=num1:
    sum2 += num2 
if num3!=num1 and num3!=num2:
    sum2 += num3
print("sum of three nubers is :",sum1)
print("sum of three different nubers is :",sum2)
#task 4:
num 1 = int(input("enter the value of num1:"))
num 2 = int(input("enter the value of num2:"))
if num1%num2 == 0:
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by",num2)
#task 5:
num1 = int(input("enter the value of num1:"))
num2 = int(input("enter the value of num2:"))
sign = input("enter the value of sign(+,-,*,/,//,%,**) :")
result = 0
if sign == "+":
    result=num1+num2
elif sign =="-":
    result=num1-num2
elif sign =="*":
    result=num1*num2 
elif sign =="/":
    result= num1/num2
elif sign =="//":
    result=num1//num2
elif sign =="%":    
    result=num1%num2    
elif sign =="**":
    result=num1**num2   
print("result of",num1,sign,num2,"is :",result)
#task 6:
num1 = int(input("enter the value of num1:"))
num2 = int(input("enter the value of num2:"))
num3 = int(input("enter the value of num3:"))
if num1<=num2 and num1<=num3:
    if num2<=num3:
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)   
elif num2<=num1 and num2<=num3:
    if num1<=num3:
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)
else:
    if num1<=num2:
        print(num3,num1,num2)
    else:
        print(num3,num2,num1)  
# task 7:
word = input("enter the letter :")
for i in word:
    if "A"<= word <="Z":
        print("litter is in uppercase")
    elif "a"<=word<="z":
        print("letter is lowercase")
    elif "0"<=word<="9":
        print("letter is digit")
    else:
        print("letter is special character")
#task 8:
# take factorial for sber security for given condition
try :
    fact = int(input("enter the factorial : "))
    f=1
    if fact>20 :
        print("enter the value less than 20 because of limited memory :",fact)
    elif fact == 0:
        print(f"factorial {fact} is 1 ")
    elif fact<0:
        print("nagative value  no factoral")
    else:
        for i in range (1,fact+1):
            f*=i
        print (f"facrtorial {fact} is {f}")
except ValueError:
    print("enter the valid value")











