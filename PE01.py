# Problem 1
# Given a non-negative integer num, return the number of steps to reduce it to zero.
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from
# it.

num = int(input("Enter an integer: "))
output_steps = 0
while num > 0:
    if num % 2 == 0:
        num /= 2
        output_steps += 1

    else:  
        num -= 1
        output_steps += 1

print(output_steps)




# Problem 2
# Given a non-negative integer number, repeatedly add all its digits until the result has only one digit. 
num = int(input("Input an positive number:"))
while num > 9:
    num = sum(map(int, str(num)))
print(num)





# Problem 3: Reverse String
# Write a function that reverses a string. The input string is given as an array of characters char[].
word = input("Enter a word here: ")

length = len(word) 
backwards_Word = word[length::-1] 
print (backwards_Word)
