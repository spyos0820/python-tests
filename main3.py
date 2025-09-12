import random

subjects = ["The cat", "My friend", "A programmer", "The teacher", "An astronaut"]
verbs = ["eats", "writes", "builds", "finds", "sees"]
objects = ["a book", "the code", "a pizza", "the answer", "a spaceship"]

sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + "."

words = sentence.split()

print('do you want to play a game?')
a = input()
if a == 'yes':
    print('Do you want to play what is in the sentence?')
    b = input()
    if b == 'yes':
        while True:
            print('Make your guess!')
            x = input()
            if x in sentence:
                position = words.index(x) + 1
                print(x,'is in the sentence on place number', position)
            else :
                hint = random.choice(words)
                print(x,'is not in the sentence')
                print('one of the words is :',hint)
                print('Do you want to keep going?')
                z = input()
                if z == 'no':
                    print('The sentence was :', sentence)
                    print("Then let's do somthing else")
                    break
                else:   
                    print('lets keep going then!')
    else :
        print('Do you want to play guess a number between 1-10?')
        f = input()
        if f == 'yes':
            while True:
                print('Make your guess!')
                d = random.randrange(1, 10)
                c = input()
                if c == d :
                    print('You guessed right!')
                    print('Do you want to keep going?')
                    z = input()
                    if z == 'no':
                        print("Then let's do somthing else")
                        break
                    else:
                        print('lets keep going then!')
                else:
                    print('You were wrong the random number was:', d)
                    print('Do you want to keep going?')
                    z = input()
                    if z == 'no':
                        print("Then let's do somthing else")
                        break
                    else:
                        print('lets keep going then!')
        else :
             while True:
                print("between 1 and 100 then!")
                print('Make your guess!')
                e = random.randrange(1, 100)
                g = input()
                if e == g:
                    print('You guessed right!!!')
                    print('Do you want to keep going?')
                    z = input()
                    if z == 'no':
                        print("Then let's do somthing else")
                        break
                    else:
                        print('lets keep going then!')
                else: 
                    print('Your guess is wrong the number was :', e)
                    print('Do you want to keep going?')
                    z = input()
                    if z == 'no':
                        print("Then let's do somthing else")
                        break
                    else:
                        print('lets keep going then!')
else:
    print("Then i can't help you any further.")