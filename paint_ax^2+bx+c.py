import base64
import numpy as np
import matplotlib.pyplot as plt
from bottle import route, run, template

@route('/fx/<min>/<max>/<step>/<a>/<b>/<c>/<a2>/<b2>/<c2>/<style>')
def index(min,max,step,a,b,c,a2,b2,c2,style):
   
    min=float(min)
    max=float(max)
    step=float(step)
    step=int((max-min)/step)
    a=float(a)
    b=float(b)
    c=float(c)
    a2=float(a2)
    b2=float(b2)
    c2=float(c2)
    style=int(style)
    x = np.linspace(min, max, step)
    y1=x*x*a+x*b+c
    y2=x*x*a2+x*b2+c2
 
    # figureを生成する
    fig = plt.figure()
 
    # axをfigureに設定する
    ax = fig.add_subplot(1, 1, 1)
    if style == 0:
        plt.plot(x, y1, marker=".", c="blue", linestyle='None')
        plt.plot(x, y2, marker=".", c="red", linestyle='None')
    else:
        plt.plot(x, y1, marker=".", c="blue")
        plt.plot(x, y2, marker=".", c="red")



 
    fig.savefig("img.png")

    file_data = open("./img.png", "rb").read()
    img_data = base64.b64encode(file_data).decode('utf-8')
    return template('ans-fx.html',img=img_data,y1=y1,y2=y2)

run(host='localhost', port=2)