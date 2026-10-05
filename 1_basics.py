 #1- write aprogram to input a welcomr messageand print it
message = input("please enter the message:")
print("hello your message is:", message) 
#2- print to obatain threre numbers to print thier sum
print("input the values for adding three values")
num1 = int(input("enter the value:"))
num2 = int(input("enter the value:"))
num3 = int(input("enter the value:"))
sum = num1+num2+num3
print("the sum of three numbers is:",sum)
#3- calculate  area of reactangle 
print("input values for calculate area of reactangle")
length = int(input("enter the value of length:"))
breadth =int(input("enter the value of breadth:"))
area = length * breadth
print("length of rectangle = ",length)
print("breadth of reactangle = ",breadth)
print("area of rectangle",area,"m²")
#4- program to calculate bmi 
print("enter the deatails for BMI of your")
name = input("enter your name :")
height_m=float(input("enter the height:"))
weight_kg=float(input("enter the weight: "))
bmi=weight_kg/(height_m*height_m)
print(name,"---->","weight is:",weight_kg,"height is:",height_m)
print("BMI of",name,"=",bmi)
#5 -program for cube of a number
print("input the values for cube")
num = int(input("enter the no :"))
cube =num**3
print("number is : ",num)
print("cube of number is :",cube) 
# 6 -convert killometer into miles
print("input to convert km into miles")
km = int(input("enter the killometer :"))
miles = 0.621371
convert = km*miles
print("killometer is :",convert)
# 7 - convert toonnes convert in quintel and kg
print("input tonnes to convert in quanital and kg")
tonnes = int(input("enter the tonnes :"))
quintal = tonnes*10
kg = quintal*100
print("tonnes is :",tonnes)   
print("quintal is :",quintal)   
print("kg is :",kg)  
# 8 -take input of a value to swap them 
print("")
a=int(input("enter the value"))
b=int(input("enter the value"))
print("enter value :",a,",",b)
print("swap value :",b,",",a)
