#time calaculation for the program
import time
t1 = time.time()
#float a =0
#float b =199.9
for i in range(100,1000,9):
    print(i)
    pass
print("done")
t2  = time.time()
a = (t1 - t2)
print(str (a))
