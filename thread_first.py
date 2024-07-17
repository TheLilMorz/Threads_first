from threading import Thread, Lock
counter=0
counter_lock = Lock()

def increcment_counter():
    global counter
    for _ in range(1000000):
        with counter_lock:
          counter+=1

def decrecment_counter():
    global counter
    for _ in range (1000000):
        with counter_lock:
          counter-=1

thread1=Thread(target=increcment_counter)
thread2=Thread(target=decrecment_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final counter value: "+str(counter))