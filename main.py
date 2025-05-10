import random


def Guessing_Game(Maximum_attempts):
 Target_number = random.randint(0,50)
 Previous_guesses = []


 for attempt in range(1,Maximum_attempts + 1):
  User_guess = int(input("What number do you think is the target number? "))

  if User_guess in Previous_guesses:
    print("Pick another number, you have already guessed this number")
    continue 

  elif User_guess > Target_number:
    print("Your guess is too high, sorry")
    attempt = attempt + 1

  elif User_guess < Target_number:
    print("Your guess is too low, sorry")
    attempt = attempt + 1
    
  Previous_guesses.append(User_guess)
  print("You've guessed these numbers:" ,Previous_guesses)
 
  if User_guess == Target_number:
   print("You've guessed the number correctly, good job!")
   break
  
  if attempt == Maximum_attempts:
    print("Sorry, you've ran out of attempts. The target number is" , Target_number)

Guessing_Game(10)
