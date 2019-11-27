
import concurrent.futures
import random
from time import sleep
import sys

def ab(a,b,c,d,e,f,i):
    sleepTime = random.randint(0, 5)
    sleep(sleepTime)
    print(i,sleepTime)
    return i, sum([a,b,c,d,e,f]) * sleepTime

a=10
b=12
c=d=e=f=a

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    future_to_url = [executor.submit(ab,a,b,c,d,e,f,i) for i in range(10)]
    for future in concurrent.futures.as_completed(future_to_url):
            try:
                    i, done = future.result()
                    print('done', i, done)
            except:
                    print("Unexpected error:", sys.exc_info())
                    traceback.print_tb(sys.exc_info()[2])


# Sample Output:
# 1 4
# 2 0
# done 2 0
# 3 0
# done 3 0
# 1 1
# done 1 62
# 4 1
# done 4 62
# 5 2
# done 5 124
# 0 5
# done 0 310
# 6 5
# done 6 310
# 8 3
# done 8 186
# 7 5
# done 7 310
# 9 3
# done 9 186
