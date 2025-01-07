import random
# import random module

Generate = random.randint(1, 100)
# Generate a random number between 1 and 100

while True: # Infinite loop until the user guesses correctly
    
    try: 
        # Asking the user to guess a number
        Guess = input('Guess the number between 1 to 100: ')

        # If the user asks for help, display the number and continue
        if Guess.lower() == 'help':
            print(f'Oops the number is {Generate}, better luck next time!')
            continue

        # Convert the user's input to an integer
        Guess = int(Guess)

        # Check if the guess is too high, too low, or correct
        if Guess > Generate:
            print('Too high!')
        elif Guess < Generate:
            print('Too low!')
        else:
            print('Congratulations! You guessed the correct number.')
            break
    except ValueError:
         # Handle invalid input (non-numeric)
         print('Please enter valid number')
