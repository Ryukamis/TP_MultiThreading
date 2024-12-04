from multiprocessing.managers import BaseManager
import QueueManager

class Queue_Client:
    def __init__(self):

        QueueManager.register('get_Taskqueue')  
        QueueManager.register('get_Resultqueue')  
        m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra')

        m.connect()
