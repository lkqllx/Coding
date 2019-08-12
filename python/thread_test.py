import threading
import logging
import time
'''Single thread'''
# def sleep_func(num):
#     logging.info('Thread %d: started' % num)
#     time.sleep(2)
#     logging.info('Thread %d: ended' % num)
#
# if __name__ == '__main__':
#     format = '%(asctime)s: %(message)s'
#     logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
#     logging.info('Main  :before creating thread')
#     thread = threading.Thread(target=sleep_func, args=(1,))
#     logging.info('Main  :before starting thread')
#     thread.start()
#     logging.info('Main  :wait for finishing')
#     logging.info('Main  :all done')

'''Multi-thread'''
def sleep_func(num):
    logging.info('Thread %d: started' % num)
    time.sleep(2)
    logging.info('Thread %d: ended' % num)

if __name__ == '__main__':
    threads = []
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    for idx in range(1,4):
        logging.info('Main  : before started Thread %d' % idx)
        thread = threading.Thread(target=sleep_func, args=(idx,))
        threads.append(thread)
        thread.start()

    for id, thread in enumerate(threads):
        logging.info('Main  : before join the Thread %d' % (id+1))
        thread.join()
        logging.info('Main  : Join Thread %d has done!!!' % (id+1))



