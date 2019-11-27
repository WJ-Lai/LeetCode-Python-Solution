import multiprocessing as mp
import threading as td
import time


def job(q):
    print('开始计算',time.ctime())
    time.sleep(q)
    print('结束计算',time.ctime())

def multithread():
    # 要把q放入参数中,若只有q一个参数，一定要加逗号，否则会报错
    t1 = td.Thread(target=job, args=(3,))
    t2 = td.Thread(target=job, args=(4,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    multithread()
