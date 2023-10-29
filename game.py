import random


class Game()
    def __init__(self)
        self.fruits={apple'red'
                     ,orange'orange',
                     tomato'red',
                     watermelon'green',
                     'graphes''viloet'}
    def quiz(self)
        while True
            fruit,color=random.choice(list(self.fruits.items()))
            print(nenter a {} color .format(fruit))
            user=input()
            if user==color
                print(ncorrect Answer)
            else
                print(n not correct answer )
            opt=int(input(n ----enter 0 to continue the game ! otherwise enter Exit ------ ))
            if opt
                break

g=Game()
g.quiz()
print(nn)
print(Bye Bye! You are Exit the game )

