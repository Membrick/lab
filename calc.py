#!/usr/bin/python3.7

from math import *
import time

print(" _____________")
print("| Simple Calc |")
print("|_____________|")
print("|     Add     |")
print("|             |")
print(" ------------")
#start of calc
num1 =  input("Enter Number to add: ")
num2 = input("Enter second number: ")
result = float(num1) + float(num2)
abort = ["Press control c to abort", "Wating for calculating to be done"]

time.sleep(0.5)
print(abort[1])
time.sleep(1)

print("Result = " + str(result))

time.sleep(1)

#end of add and start of substract

print(" ____________") 
print("|            |")
print("|  Substract |")
print("|            |")
print(" ------------") 
print(abort[0])

time.sleep(1)


num1 = input("Enter number to Multiply: ")
num2 = input("Enter second number: ")

result = float(num1) - float(num2)

time.sleep(0.5)
print(abort[1])
time.sleep(1)  

print( "Result = " + str(result))

#end of substract  and start of devide


print(" ____________")
print("|            |")
print("|  Multiply  |")
print("|            |")
print(" ------------")
print(abort[0])

time.sleep(1)


num1 = input("Enter number to Multiply: ")
num2 = input("Enter second number: ")

result = float(num1) * float(num2)

time.sleep(0.5)
print(abort[1])
time.sleep(1)

print( "Result = " + str(result))

#end of multiply and start of devide

print(" ____________") 
print("|            |")
print("|   Devide   |")
print("|            |")
print(" ------------") 
print(abort[0])

time.sleep(1)


num1 = input("Enter number to devide: ")
num2 = input("Enter second number: ")

result = float(num1) / float(num2)

time.sleep(0.5)
print(abort[1])
time.sleep(1)  

print( "Result = " + str(result))

#end of multiply and start of devide

