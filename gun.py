import random
import time

rng1 = random.randint(1,5)
rng2 = random.randint(1,5)
bullets = 6

def shoot_func(s,x,y):
    s -= 1
    print("pew")
    time.sleep(0.25)
    shoot_func(s,x,y)
    
    if x == y:
        print("jammed...")
        time.sleep(3)
        shoot_func(s,x,y)
        
    elif x != y:
        s -= 1
        print("pew")
        time.sleep(0.25)
        shoot_func(s,x,y)
        
    elif s == 0:
        print("reloading...")
        time.sleep(2.5)
        shoot_func(s,x,y)
        
shoot_func(bullets,rng1,rng2)
