from queue_client import QueueClient
from task import Task


class Minion(QueueClient):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            Task = self.get_task(self.task_queue)
            if Task is None:
                continue

            print(f"reçu #{task.identifier}")
            task.work()
            print(f"terminé #{task.identifier} en {task.time} secondes")

            self.result_queue.put(task)


if __name__ == "__main__":
    minion = Minion()
    minion.run()
