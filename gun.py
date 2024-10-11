import random
import time

jam = random.randint(0,1)
bullets = 6
reload = 2.25

def shoot_func(x,y):
    if x == random.randint(0,1):
        print("pew")
        y = y - 1
        if y < 1:
            print("reload...")
            time.sleep(reload)
        
shoot_func(jam,bullets)
