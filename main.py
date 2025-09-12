import random
txt = 'The best things in life are free!'
print('do you want to play a game?')
a = input()
if a == 'yes':
    print('Do you want to play what is in the sentence?')
    b = input()
    if b == 'yes':
        while True:
            #print?
            x = input()
            if x in txt:
                print(x,'is in the sentence')
            else :
                print(x,'is not in the sentence')
                print('Do you want to keep going?')
                z = input()
                if z == 'no':
                    print("Then let's do somthing else")
                    break
                else:   
                    print('lets keep going then!')
    else :
        print('Guess a number between 1-10?')
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