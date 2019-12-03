from concurrent.futures import ThreadPoolExecutor
import time

def boil_udon():
    print('うどんを茹でます。')
    time.sleep(3)
    print('うどんが茹で上がりました。')

tpe = ThreadPoolExecutor(max_workers=3)

print('うどんを100個茹でます。')
for _ in range(100):
    tpe.submit(boil_udon)
tpe.shutdown()
print('うどんが１００個茹で上がりました。')