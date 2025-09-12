import random

subjects = ["The cat", "My friend", "A programmer", "The teacher", "An astronaut"]
verbs = ["eats", "writes", "builds", "finds", "sees"]
objects = ["a book", "the code", "a pizza", "the answer", "a spaceship"]

while True:  
    sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + "."
    words = sentence.split()
    clean_words = [w.strip(".,!?").lower() for w in words]

    print('Do you want to play a game? (yes/no)')
    a = input().lower()

    if a == 'yes':
        print('Do you want to play "What is in the sentence?" (yes/no)')
        b = input().lower()

        if b == 'yes':
            while True:
                x = input("Make your guess: ").lower().strip(".,!?")
                if x in clean_words:
                    position = clean_words.index(x) + 1
                    print(x, "is in the sentence on place number", position)
                else:
                    hint = random.choice(words)
                    print(x, "is not in the sentence")
                    print("One of the words is:", hint)

                z = input("Do you want to keep going? (yes/no) ").lower()
                if z == 'no':
                    print("The sentence was:", sentence)
                    print("Then let's do something else")
                    break

        else:
            print('Guess a number between 1-10!')
            d = random.randrange(1, 10)
            while True:
                c = int(input("Make your guess: "))
                if c == d:
                    print("You guessed right!")
                else:
                    print("You were wrong, the random number was:", d)

                z = input("Do you want to keep going? (yes/no) ").lower()
                if z == 'no':
                    print("Then let's do something else")
                    break

            print("Now between 1 and 100!")
            e = random.randrange(1, 100)
            while True:
                g = int(input("Make your guess: "))
                if g == e:
                    print("You guessed right!!!")
                else:
                    print("Your guess is wrong, the number was:", e)

                z = input("Do you want to keep going? (yes/no) ").lower()
                if z == 'no':
                    print("Then let's do something else")
                    break

    else:
        print("Then I can't help you any further.")

    
    again = input("Do you want to play again? (yes/no) ").lower()
    if again == 'no':
        print("Thanks for playing, bye!")
        break
