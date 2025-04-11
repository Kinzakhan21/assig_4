import random
print("Welcome to the Number Guessing Game!")

low = 1
high = 10

print("Think of a number between 1 to 10 and computer will be guss it.")

if low <= high:
    guess = random.randint(low,high)
    print("Computer's guess is:" , guess)

while True:
    feedback = input("Is the guess too high (H) , TOO low(L) or computer")
    
    if  feedback == 'C':
     print("Yay! The computer guesssed your number")
     break
    elif feedback == 'H':
        high = guess -1
        guess = random.randint(low , high)
        print("Computer's guess is: " , guess)
    elif feedback == 'L':
        low = guess +1 
        guess = random.randint(low , high)
        print("Computer's guess is: " , guess)
    else:
         print("Invalid input. Please enter H, L , OR C.")
if low > high:
    print("This number is not in the range. Please try again.")
    