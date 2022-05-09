import keyboard
import json

stop = False # переменнаяя для прерывания цикла в случае неправильного шага
x = 0 # переменная для того, чтобы KEY_DOWN обрабалтывалась функцией, а KEY_UP нет
y = False # переменная для отсечки нажатия клавиш, отличных от стрелок управления

# добавил класс, хотя без него можно было обойтись, но в условии было сказано использовать ООП...
class choise():
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

# функция обрабатывающая нажатие клавиши (управление Шариком осуществляется курсором)
def step(key):
    global x, y
    x +=1
    if x%2 == 1:
        res = 0
        if key == 'up':
            res = route[int(i)].up
        elif key == 'down':
            res = route[int(i)].down
        elif key == 'left':
            res = route[int(i)].left
        elif key == 'right':
            res = route[int(i)].right
        else:
            print('\nДля управления Шариком используйте стрелки.\n')
        global stop
        if 2 <= res <= 4:
            stop = True
        else:
            stop = False
        if res == 1 or res == 2 or res == 3 or res == 4:
            print(res_text[res])
            y = True
        else:
            y = False

# правильный маршрут Шарика
route = [choise(4,4,4,1),choise(2,1,3,2),choise(3,2,1,2),choise(2,1,2,3),
         choise(3,2,2,1),choise(2,4,3,1),choise(2,2,3,1),choise(4,2,3,1),
         choise(4,1,3,2),choise(3,1,4,2),choise(3,2,2,1),choise(2,4,3,1),
         choise(2,2,3,1),choise(2,2,3,1),choise(2,1,3,2),choise(3,2,1,2),
         choise(2,1,2,3),choise(3,1,2,4),choise(3,2,1,2),choise(2,1,2,3),
         choise(3,2,4,1),choise(2,1,3,2),choise(3,2,2,1)]

# словарь с сообщениями-результатами
res_text = {1:'Шарик на верном пути',
            2:'Шарик ударился о стену',
            3:'Шарик струсил и убежал',
            4:'Шарик заблудился',
            }

print('Помогаем Шарику найти косточку.')
s = 0
with open('save.json', 'r') as read_file:
    st = json.load(read_file)
if st == {} or st == 0:
    print('Сделайте первый шаг:')
else:
    save = input('Есть сохранённый результат предыдущей игры, начать игру с сохранённой позиции? (y/n).\n')
    if save == 'y':
        s = int(st)
        print('Сделайте следующий шаг, после сохранения:')
    else:
        s = 0
        print('Сделайте первый шаг:')
for i in range(s,len(route)):
    y = False
    while y == False:
        step(keyboard.read_key())
    if stop == True:
        print('Игра окончена!')
        yn = input('Хотите сохранить пройденный маршрут? (y/n)\n')
        if yn == 'y':
            with open('save.json', 'w') as write_file:
                json.dump(i, write_file)
        else:
            with open('save.json', 'w') as write_file:
                json.dump(0, write_file)
        break
    elif stop == False and x%2 == 1:
        print('Сделайте следующий шаг:')
        continue
if stop == False:
    print('Поздравляем с победой!')


# 80% времени убил на разбор того, как считывать кнопки курсора... и всё равно выглядит как-то криво...
# должен быть более простой метод считывания нажатия на python, буду благодарен, если подскажите мне его.