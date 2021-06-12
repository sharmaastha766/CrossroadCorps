import time
def timer(t,s):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        #print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("light changes to "+s)
    
l=["red","yellow","green"]
print("Traffic light starts with red")
try:
    while True:
        timer(30,l[1])
        timer(10,l[2])
        timer(30,l[0])
except KeyboardInterrupt:
    pass
#Press ctrl+c to kill the timer 
