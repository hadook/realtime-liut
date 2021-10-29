
class Scheduler:
    """ Class to represent a scheduler object that calculates the optimal order for task execution. """

    # initializes an instance of a scheduler object
    def __init__(self, tasks):
        self.tasks = tasks
        self.time = 0
        self.order = []

    # runs the task ordering algorithm
    def order_tasks(self):
        self.order = []
        while self.count_tasks():
            # set task to be processed
            current_task = None
            for task in self.tasks:
                if task.active(self.time):
                    if current_task is None:
                        current_task = task
                    elif task.deadline < current_task.deadline:
                        current_task = task

            # advance time and task
            if current_task is not None:
                current_task.advance(self.time)
                if current_task.completed:
                    self.order.append((self.time, current_task.name, True))
                else:
                    self.order.append((self.time, current_task.name, False))
            else:
                self.order.append((self.time, "idle", False))
            self.time += 1

    # returns number of tasks yet to be completed
    def count_tasks(self):
        counter = 0
        for task in self.tasks:
            if not task.completed:
                counter += 1
        return counter

    # returns a string timestamp [startTime-endTime]
    def get_timestamp(self):
        return "[" + str(self.time) + "-" + str(self.time + 1) + "]"

    # prints basic attributes for each task
    def print_tasks(self):
        print("\nTasks [p,r,d]:")
        for task in self.tasks:
            print(task.name, [task.processing, task.release, task.deadline])

    # prints scheduled task execution timeline
    def print_scheduling(self):
        print("\nScheduling:")
        for item in self.order:
            timestamp = "[" + str(item[0]) + "-" + str(item[0] + 1) + "]"
            task = item[1]
            completed = "(completed)" if item[2] else ""
            print(timestamp, task, completed)

    # prints scheduled task execution timeline to string
    def str_scheduling(self):
        out = "\nScheduling:"
        for item in self.order:
            timestamp = "[" + str(item[0]) + "-" + str(item[0] + 1) + "]"
            task = item[1]
            completed = "(completed)" if item[2] else ""
            out += "\n" + timestamp + "\t" + task + "\t" + completed
        return out

    # prints the late attribute for each task
    def print_lateness(self):
        l_max = 0
        print("\nLateness:")
        for task in self.tasks:
            print(task.name, task.late)
            if task.late > l_max:
                l_max = task.late
        print("Lmax:", l_max)

    # prints the late attribute for each task to string
    def str_lateness(self):
        l_max = 0
        out = "\nLateness:"
        for task in self.tasks:
            out += "\n" + task.name + "\t" + str(task.late)
            if task.late > l_max:
                l_max = task.late
        out += "\n" + "Lmax = " + str(l_max)
        return out

    # prints the execution timeframe for each task
    def print_timeframes(self):
        print("\nExecution timeframes:")
        for task in self.tasks:
            print(task.name, task.timeframes)
