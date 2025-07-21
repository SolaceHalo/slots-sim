import random

money = 100 #starting money
print('you start with %d dollars' % money)

firstNumber = random.randint(1,10) #initial first number
print('first number: %d' % firstNumber)
secondNumber = random.randint(1,10) #initial second number
print('second number: %d' % secondNumber)
thirdNumber = random.randint(1,10) #initial third number
print('third number: %d' % thirdNumber)

while money > 0:
    if firstNumber == secondNumber == thirdNumber: #first, second, and third number are equal
        print('you win!')
        money = money + 100
        print('you get %d' % money)
        break
    else: #at least one number differs
        money = money - 10 #user loses 10 dollars
        print('current money: %d' % money) #money after roll
        print('try another roll!')
        state = input('do you want to continue? press y for yes, n for no ')
        if state == 'y':
                firstNumber = random.randint(1,10) #generates new numbers
                print('first number: %d' % firstNumber)
                secondNumber = random.randint(1,10)
                print('second number: %d' % secondNumber)
                thirdNumber = random.randint(1,10)
                print('third number: %d' % thirdNumber)
                continue #continue game
        elif state == 'n':
                print('final money: %d' % money) #final money total
                break #end game
        else: #just in case someone types something other than y or n
                print('this is a fail safe')
                break

if money == 0: #user fails to get first = second = third
    print('your game is over. better luck next time!')
