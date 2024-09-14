import math
def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if n % i== 0:

            return False

    return True 
name = input ("Enter you are name")

num1 =int(input("Enter farst favraet number:"))
num2 =int(input("Enter saecond favraet number:"))
num3 =int(input("Enter thered favraet number:"))

numbers = [num1,num2,num3]

even_odd_list=[]
for num in numbers:
    if num % 2 == 0:
        even_odd_list.append((num, "even"))
    else:
        even_odd_list.append((num, "odd"))

print (f"Hallo{name}! let's explore your favorite numbers:")

for num, even_odd in even_odd_last:
    print (f"the number {num} is {even_odd}.")

for num in numbers:
    print(f"The number {num} and its square: ({num}, {num ** 2})")

    total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}") 

if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")

else:
    print(f"{total_sum} is not a prime number, but it's still great!")