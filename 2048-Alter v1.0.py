#2048-Alter by Welkin Mario
#contact: YUHO(Wechat), or Welkin_M(Steam)
    #email: yuhosan@163.com
#recommend to have a look at README

from random import *

# initialize the grid
x1 = [0]*4
x2 = [0]*4
x3 = [0]*4
x4 = [0]*4
x  = [x1,x2,x3,x4]
# define how the game runs
rand = [2,4]
control = ['w','s','a','d', 'retry']
intro = '''please input w/a/s/d and press Enter to move
or retry to play again or esc to close the window'''
# for inproper input
message = [intro, 'Come on',
	'only w/a/s/d can be used to move or "esc" to exit or "retry" to replay',
	'hey, you can look at the first line for help', 
	'intentionally taping properly is not funny, dude',
	'MAYBE YOU SHOULD TRY lowercase',
	'you can input "retry" to play again if you are stuck']

def cha(x):# randomly generate a number in the grid
    con = True
    while con:
        for i in range(4):
            if 0 in x[i]:
                a = randrange(4)
                b = randrange(4)
                if x[a][b] == 0:
                    x[a][b] = choice(rand)
                    con = False
                    break
    return x

score= 0
turn = 1 # make sure the game can continuosly run and record turns

# display the initial grid
print('Turn: ', turn, '    Score: ', score)
cha(x)
cha(x)# generate two number at start
for i in range(4):
    print(x[i])
print(intro)

# mothod to calculate and move
while turn:
    move = input('What is next:')
    if move == 'esc':# for exit the program
        break
    elif move in control:
        if move == 'retry':# play again
            score= 0
            turn = 1
            for i in range(4):
                for j in range(4):
                    x[i][j] = 0
        if move == 'w' :# move up all numbers
            turn += 1
            for i in range(3):# move forward three times
                for a in [0,1,2]:# zero, if any, will be put back
                    for b in range(4):
                        if x[a][b] == 0:
                            x[a][b] = x[a+1][b]
                            x[a+1][b] = 0
            for a in [0,1,2]:# add up same number
                for b in range(4):
                    if x[a][b] == x[a+1][b]:
                        x[a][b] += x[a+1][b]
                        score += x[a][b]
                        x[a+1][b] = 0
            for a in [0,1,2]:# eliminate blank square
                for b in range(4):
                    if x[a][b] == 0:
                        x[a][b] = x[a+1][b]
                        x[a+1][b] = 0
        if move == 's':# down
            turn += 1
            for i in range(3):
                for a in [3,2,1]:
                    for b in range(4):
                        if x[a][b] == 0:
                            x[a][b] = x[a-1][b]
                            x[a-1][b] = 0
            for a in [3,2,1]:
                for b in range(4):
                    if x[a][b] == x[a-1][b]:
                        x[a][b] += x[a-1][b]
                        score += x[a][b]
                        x[a-1][b] = 0
            for a in [3,2,1]:
                for b in range(4):
                    if x[a][b] == 0:
                        x[a][b] = x[a-1][b]
                        x[a-1][b] = 0
        if move == 'a':# left
            turn += 1
            for i in range(3):
                for a in range(4):
                    for b in [0,1,2]:
                        if x[a][b] == 0:
                            x[a][b] = x[a][b+1]
                            x[a][b+1] = 0
            for a in range(4):
                for b in [0,1,2]:
                    if x[a][b] == x[a][b+1]:
                        x[a][b] += x[a][b+1]
                        score += x[a][b]
            for a in range(4):
                for b in [0,1,2]:
                    if x[a][b] == 0:
                        x[a][b] = x[a][b+1]
                        x[a][b+1] = 0
        if move == 'd':# right
            turn += 1
            for i in range(3):
                for a in range(4):
                    for b in [3,2,1]:
                        if x[a][b] == 0:
                            x[a][b] = x[a][b-1]
                            x[a][b-1] = 0
            for a in range(4):
                for b in [3,2,1]:
                    if x[a][b] == x[a][b-1]:
                        x[a][b] += x[a][b-1]
                        score += x[a][b]
                        x[a][b-1] = 0
            for a in range(4):
                for b in [3,2,1]:
                    if x[a][b] == 0:
                        x[a][b] = x[a][b-1]
                        x[a][b-1] = 0
        cha(x)# again change the grid and print
        print('Turn: ', turn, '    Score: ', score)
        for i in range(4):
            print(x[i])
        print()
        # judge if there is blank square;if not, game over
        if 0 not in x1:
            if 0 not in x2:
                if 0 not in x3:
                    if 0 not in x4:
                        print('Game Over, please retry')
    else:
        print(choice(message))

