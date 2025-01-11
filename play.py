
import random
import pyautogui as py

positions = { "collect": (500,213)  }

c = (492, 423)
while True:
    for i in range( 300 ):
        py.PAUSE = 0.001

        py.click(x=c[0],y=c[1])
        py.click(x=positions['collect'][0],y=positions['collect'][1])
        py.click(x=random.randrange(150,900,30),y=640)
    py.click(x=1500,y=500)
    a = input( '> ' )
