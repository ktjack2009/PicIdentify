import numpy as np
from PIL import Image
import time

def _(list_obj):
    # 去除自身重复的
    type_1 = ()
    type_2 = ()
    type_3 = ()
    for i in list_obj:
        if not type_1:
            type_1 = i
        else:
            if np.abs(type_1[0]-i[0]) + np.abs(type_1[1]-i[1]) < 15:
                # 同一类
                pass
            else:
                if not type_2:
                    type_2 = i
                else:
                    if np.abs(type_2[0]-i[0]) + np.abs(type_2[1]-i[1]) < 15:
                        pass
                    else:
                        if not type_3:
                            type_3 = i
    result = [type_1, type_2, type_3]
    return [i for i in result if i]

def get_x_y(circle_x_y, star_x_y, square_x_y):
    dict_obj = {}
    for _ in range(3):
        if len(circle_x_y) == 1:
            dict_obj[u'圆点'] = circle_x_y[0]
        if len(star_x_y) == 1:
            dict_obj[u'星形'] = star_x_y[0]
        if len(square_x_y) == 1:
            dict_obj[u'方块'] = square_x_y[0]

        if len(circle_x_y) > 1:
            for i in circle_x_y.copy():
                
                if dict_obj.get('星形'):
                    if np.abs(dict_obj.get('星形')[0]-i[0]) + np.abs(dict_obj.get('星形')[1]-i[1]) < 15:
                        circle_x_y.remove(i)
                if dict_obj.get('方块'):
                    if np.abs(dict_obj.get('方块')[0]-i[0]) + np.abs(dict_obj.get('方块')[1]-i[1]) < 15: 
                        circle_x_y.remove(i)


        if len(star_x_y) > 1:
            for i in star_x_y.copy():
                if dict_obj.get('圆点'):
                    if np.abs(dict_obj.get('圆点')[0]-i[0]) + np.abs(dict_obj.get('圆点')[1]-i[1]) < 15:
                        star_x_y.remove(i)
                if dict_obj.get('方块'):
                    if np.abs(dict_obj.get('方块')[0]-i[0]) + np.abs(dict_obj.get('方块')[1]-i[1]) < 15: 
                        star_x_y.remove(i)

        if len(square_x_y) > 1:
            for i in square_x_y.copy():
                if dict_obj.get('星形'):
                    if np.abs(dict_obj.get('星形')[0]-i[0]) + np.abs(dict_obj.get('星形')[1]-i[1]) < 15:
                        square_x_y.remove(i)
                if dict_obj.get('圆点'):
                    if np.abs(dict_obj.get('圆点')[0]-i[0]) + np.abs(dict_obj.get('圆点')[1]-i[1]) < 15: 
                        square_x_y.remove(i)
    return dict_obj
    
circle = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])
star = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
])
square = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])
SIZE = 13
THRESHOLD_VALUE_1 = 0.83
THRESHOLD_VALUE_2 = 0.85
THRESHOLD_VALUE_3 = 0.90

im = Image.open('./pic_9.png')
im.show()
im = im.convert('L')
im = np.where(np.array(im) > 250, 1, 0)
dict_obj = {}

circle_x_y = []
star_x_y = []
square_x_y = []
for x in range(0, im.shape[0] - SIZE, 2):
    for y in range(im.shape[1] - SIZE):
        part = im[x: x + SIZE][:, y: y + SIZE]
        if np.average(part == star) > THRESHOLD_VALUE_1:
            # dict_obj[u'星形'] = y + int(SIZE / 2), x + int(SIZE / 2)
            star_x_y.append((y + int(SIZE / 2), x + int(SIZE / 2)))
        if np.average(part == circle) > THRESHOLD_VALUE_2:
            # dict_obj[u'圆点'] = y + int(SIZE / 2), x + int(SIZE / 2)
            circle_x_y.append((y + int(SIZE / 2), x + int(SIZE / 2)))
        if np.average(part == square) > THRESHOLD_VALUE_3:    
            # dict_obj[u'方块'] = y + int(SIZE / 2), x + int(SIZE / 2)
            square_x_y.append((y + int(SIZE / 2), x + int(SIZE / 2)))

# print(circle_x_y)
# print('111')
# print(star_x_y)
# print('111')
# print(square_x_y)
t0 = time.time()
circle_x_y = _(circle_x_y)
star_x_y = _(star_x_y)
square_x_y = _(square_x_y)

# print('------\n\n')
# print(circle_x_y)
# print('111')
# print(star_x_y)
# print('111')
# print(square_x_y)
print(get_x_y(circle_x_y, star_x_y, square_x_y))
# print(time.time() - t0)