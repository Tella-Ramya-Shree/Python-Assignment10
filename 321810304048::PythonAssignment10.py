#1. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".For numbers which are multiples of both three and five print "FizzBuzz".
i=1
while (i<= 100):
    if i%3==0:
        print("Fizz", end="")
        if (i%5==0):
            print("Buzz", end="")
    elif (i%5==0):
         print("Buzz", end="")
    else:
         print(i, end="")
    print()
    i+=1
#Output:-
#1           11             Fizz      31
#2           Fizz           22        32
#Fizz        13             23        Fizz
#4           14             Fizz      34
#Buzz       FizzBuzz        Buzz      Buzz
#Fizz        16             26        Fizz  
#7           17             Fizz      37
#8           Fizz           28        38
#Fizz        19             29        Fizz 
#Buzz        Buzz           FizzBuzz  FizzBuzz......

#2.Write a Python program to remove consecutive duplicates from list.
list = [1,1,1,1,1,1,2,3,4,4,5,6,7,7,8]
print("Original list:\n",list) 
i = 0
while i < len(list)-1:
    if list[i] == list[i+1]:
        del list[i]
    else:
        i = i+1
print("After removing consecutive duplicates:\n",list)
#Output:-
#Original list:
#  [1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 1, 2]
#After removing consecutive duplicates:
#  [1, 2, 3, 4, 5, 1, 2]

#3. Write a python program to find unique element from a list.
my_list = [1,2,3,3,4,5,2,1,8]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)
#Output:-
#Original List :
#  [1, 2, 3, 3, 4, 5, 2, 1, 8]
#List of unique numbers :
#  [1, 2, 3, 4, 5, 8]

#4.Write a function that checks whether a number is in a given range(inclusive of high and low) 
 def ran_check(low,high,num):
    for i in range(low,high+1):
        if num==i:
            print (num,'number is within the range')
            break
    else :
            print(num,'number is out of range')
low=int(input('Enter the starting range:'))
high=int(input('Enter the ending range:'))
num=int(input('Enter the number:'))
ran_check(low,high,num)

#Output:-
#CASE1:
#Enter the starting range:1
#Enter the ending range:20
#Enter the number:13
#13 number is within the range

#CASE2:
#Enter the starting range:1
#Enter the ending range:20
#Enter the number:27
#27 number is out of range

#5.Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    ucount=0
    lcount=0
    for letter in s:
            if str.isupper(letter):
                ucount+=1
            elif str.islower(letter):
                lcount+=1
    print('Count of upper case characters in string is ',str(ucount))
    print('Count of lower case characters in string is ',str(lcount))
s=input('Enter the string:')
up_low(s)
#Output:-
#Enter the string:Gitam School Of Technology,Bangalore,Karnataka
#Count of upper case characters in string is  6
#Count of lower case characters in string is 35









