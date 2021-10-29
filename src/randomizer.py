import random
from task import Task


class Randomizer:
    """ Class to generate a random set of tasks for visualization. """

    def __init__(self, num_tasks=0):
        self.tasks = []
        Task.num_tasks = 0
        if num_tasks == 0:
            num_tasks = random.randint(5, 10)
        for i in range(0, num_tasks):
            self.tasks.append(self.generate_task(num_tasks))

    @staticmethod
    def generate_task(num_tasks):
        p = random.randint(1, 4)
        r = random.randint(0, int(num_tasks * 0.8))
        d = r + p + random.randint(0, num_tasks)
        return Task(p, r, d)
