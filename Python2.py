import time
import threading

def boil_udon():
    print('うどんを茹でます。')
    time.sleep(3)
    print('うどんが茹で上がりました。')

def make_tuyu():
    print('つゆを作ります')
    time.sleep(2)
    print('つゆができました。')

print('うどんを作ります')
thread1 = threading.Thread(target=boil_udon)
thread2 = threading.Thread(target=make_tuyu)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('盛り付けます。')
print('うどんができました。')
