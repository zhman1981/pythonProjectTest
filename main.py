import keyboard

stop = 0
x = 0

class choise():
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

def step(key):
    global x
    x +=1
    if x%2 == 1:
        res = 0
        k = float(i/2)
        if key == 'up':
            res = route[int(k)].up
        elif key == 'down':
            res = route[int(k)].down
        elif key == 'left':
            res = route[int(k)].left
        elif key == 'right':
            res = route[int(k)].right
        print(res_text[res])
        global stop
        if 2 <= res <= 4:
            stop = 1
        else:
            stop = 0

route = [choise(4,4,4,1),choise(2,1,3,2),choise(3,2,1,2),choise(2,1,2,3),
         choise(3,2,2,1),choise(2,4,3,1),choise(2,2,3,1),choise(4,2,3,1),
         choise(4,1,3,2),choise(3,1,4,2),choise(3,2,2,1),choise(2,4,3,1),
         choise(2,2,3,1),choise(2,2,3,1),choise(2,1,3,2),choise(3,2,1,2),
         choise(2,1,2,3),choise(3,1,2,4),choise(3,2,1,2),choise(2,1,2,3),
         choise(3,2,4,1),choise(2,1,3,2),choise(3,2,2,1)]

res_text = {1:'Шарик на верном пути',
            2:'Шарик ударился о стену',
            3:'Шарик струсил и убежал',
            4:'Шарик заблудился',
            }

print('Помогаем Шарику найти косточку.\nСделайте первый шаг.')

for i in range(len(route)*2):
    step(keyboard.read_key())
    if stop == 1:
        print('Игра окончена!')
        break
    elif stop == 0 and x%2 == 0:
        print('Сделайте следующий шаг:')
        continue

print('Поздравляем с победой!')