import QueueManager
from task import Task,work
import QueueClient

class Minion(Queue_Client):
    def __init__(self):
        super.__init__()



    if __name__ == '__main__':
        queue_=self.task_queue.get()

        task_minion=queue.get()
        result=work(task_minion)
        queue.set_result_queue(result)
