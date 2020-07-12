import numpy as np

def act(x):
    return 0 if x<0.5 else 1

def go(floor, room, price):
    x = np.array([floor, room, price])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    we1 = np.array([w11, w12])
    we2 = np.array([-1, 1])

    s = np.dot(we1, x)
    print("Sum: " + str(s))

    o = np.array([act(x) for x in s])
    print("Output: " + str(o))

    es = np.dot(we2, o)
    y = act(es)
    print("Res: " + str(y))

    return y

floor = 1
room = 0
price = 1

res = go(floor, room, price)
if res == 1:
    print("Ok")
else:
    print("Fail")
