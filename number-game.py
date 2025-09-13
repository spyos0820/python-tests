import random
import time

def guessing_game(limit):
    number = random.randrange(1, limit + 1)  
    #print(f"(debug: het geheime getal is {number})")  

    while True:
        y = input(f"Guess a number between 1 and {limit}: ")

        if y.lower() == 'exit':
            print("Then let's do something else")
            return False  
        try:
            k = int(y)
        except ValueError:
            print("Please enter a number or type 'exit' to quit.")
            continue

        if k < number:
            print("Higher!")
            time.sleep(1)
        elif k > number:
            print("Lower!")
            time.sleep(1)
        else:
            print("🎉 You guessed right! Well done!")
            return True  



if guessing_game(10):        
    print("Let's make it harder!")
    time.sleep(1)
    if guessing_game(100):   
        print("🔥 You're really good! Final challenge...")
        time.sleep(1)
        guessing_game(1000)  
