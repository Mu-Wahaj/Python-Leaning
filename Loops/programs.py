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
while command.lower() != "quit":
    command = input("Enter a command (start, stop, quit): ")
    if command.lower() == "start":
        print("Car started.")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command.lower() == "quit":
        print("Exiting the game.")
    else:
        print("Invalid command. Please enter 'start', 'stop', or 'quit'.")