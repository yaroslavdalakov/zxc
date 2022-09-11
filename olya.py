from random import randint
game = True
num = randint(1,100)

file = open('game_result','w',encoding='utf8')


print('попробуй угадать число от 1 до 100')
file.write('попробуй угадать число от 1 до 100\n')
while game:
    g = int(input('введите предположение: '))
    file.write(f'введите предположение: {g}\n')
    if g == num:
        print('вы угадали верно!')
        file.write('вы угадали верно!\n')
        game = False
    elif g < num:
        print(f"неверно,попробуй число больше чем {g}")
        file.write(f"неверно,попробуй число больше чем {g}\n")
    elif g > num:
        print(f"неверно,попробуй число меньше чем {g}")
        file.write(f"неверно,попробуй число меньше чем {g}\n")

file.close()
file.closed
        
