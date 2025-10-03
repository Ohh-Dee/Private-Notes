# timer program
import time
# if you want to use a default argument make sure there after the arugement thats passed in
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done.")
    
count(15)