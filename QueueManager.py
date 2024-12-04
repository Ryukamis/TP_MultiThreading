from multiprocessing.managers import BaseManager

from queue import Queue

task_queue = Queue()
result_queue = Queue()

class QueueManager(BaseManager): pass

    
if __name__ == '__main__':    
    QueueManager.register('task_queue')
    QueueManager.register('result_queue')
    m = QueueManager(address=('', 50000), authkey=b'abracadabra')

    s = m.get_server()

    s.serve_forever()