import threading
import queue
import time
import random 

MAXT = 4
'''
class MyThread(threading.Thread):
    def run(self, shared):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        shared._print(self.name)
        time.sleep(random.randrange(1,3))                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"

'''
lock = threading.RLock()

class Cache(object):
    def __init__(self):
        self._count = 0

    def use(self, who):
        with lock:
            print("{} using cache-use-!".format(who))
            time.sleep(random.randrange(2,4))
            self._count += 1
            self.use_due(who)
            print("{} finished cache-use-!".format(who))

    def use_due(self, who):
        with lock:
            print("{} using cache-use_due-!".format(who))
            self._count += 2
            time.sleep(random.randrange(1,2))
            print("{} finished cache-use_due-!".format(who))


def f(x):
    return x*x

def process_item(item, who, result_queue):
    print("{} started!".format(who))              # "Thread-x started!"
    item.use(who)                                     # Pretend to work for a second
    result_queue.put((who, item))
    print("{} finished!".format(who))             # "Thread-x finished!"
    #lock.release()

#process_item(None)
def main():
    pool = []
    q = queue.Queue()
    
    for x in range(20):                                     # Four times...
        if len(pool)>= MAXT:
            try:
                result1 = q.get()
                pool = [t for t in pool if t.isAlive()]
                print(result1)
            except:
                print("An exception occurred")

        c = Cache()
        mythread =  threading.Thread(name= "Thread-{}".format(x + 1), target=process_item, args=(c, "Thread-{}".format(x + 1), q))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, invoke the run method
        pool.append(mythread)
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another
        print('num threads: %s'%str(len(pool)))

    while len(pool):
     '''   
    print(pool)
    #for t in pool:
    #    t.join()
    '''
    


    print('main_end')
    


if __name__ == '__main__':main()