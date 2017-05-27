#!/usr/bin/python
# coding: utf-8
import multiprocessing, time
def run():
    i = 0;
    while i < 10:
        print('running'); time.sleep(2)
        i += 1
if __name__ == '__main__':
    p = multiprocessing.Process(target=run)
    p.start()
    # p.join()
    print(p.pid)
    print('master gone')

