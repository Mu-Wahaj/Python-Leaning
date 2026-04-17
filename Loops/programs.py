# This code implements a simple number guessing game. The user has a limited number of attempts to guess a secret number. If the user guesses correctly, they win; otherwise, they lose after exhausting all attempts.
secret_number = 7
gussed_count = 0
gussed_limit = 3
while gussed_count < gussed_limit:
    gussed_number = int(input("Guess the secret number: "))
    gussed_count += 1
    if gussed_number == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
else:
    print("Sorry, you've used all your guesses.")
print("The secret number was:", secret_number)

#exercise question to print the multiplication table of a given number using for loop
number = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    
    
    
    # car game using while loop
command = ""
started = False

while True:
    command = input(">").lower()
    if command == "start":
        if not started:
            print("Car started...Ready to go!")
            started = True
        else:
            print("Car is already started.")
    elif command == "stop":
        if started:
            print("Car stopped.")
            started = False
        else:
            print("Car is already stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "quit":
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Sorry, I don't understand that command.")

#funtion to calculate the factorial of a number using a for loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}.")