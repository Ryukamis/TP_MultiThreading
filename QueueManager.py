from multiprocessing.managers import BaseManager

from queue import Queue

task_queue = Queue()
result_queue = Queue()

class QueueManager(BaseManager):
    def __init__(self, url: str, port: int, authkey: bytes):
        super().__init__(address=(url, port), authkey=authkey)

        self.task_queue = mp.Queue()
        self.result_queue = mp.Queue()

        self.register("get_task_queue", callable=lambda: self.task_queue)
        self.register("get_result_queue", callable=lambda: self.result_queue)
        
    def serve(self):
        print(f"Starting server at {self.address[0]}:{self.address[1]} ...")
        s = self.get_server()
        s.serve_forever()
    
if __name__ == "__main__":
    manager = QueueManager("localhost", 50000, b"abc123")
    manager.serve()
