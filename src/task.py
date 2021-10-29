
class Task:
    """ Class to represent an instance of a non-periodic, divisible task. """
    num_tasks = 0
    colors = ['indianred', 'cornflowerblue', 'gold', 'springgreen', 'orchid',
              'chocolate', 'skyblue', 'khaki', 'forestgreen', 'darkorchid']

    # initializes an instance of an object
    def __init__(self, processing, release, deadline):
        self.name = "Z" + str(Task.num_tasks + 1)
        self.color = Task.colors[Task.num_tasks % 10]
        self.processing = processing
        self.release = release
        self.deadline = deadline
        self.progress = 0
        self.late = 0
        self.completed = False
        self.timeframes = []

        Task.num_tasks += 1

    # returns Boolean to indicate whether the task is available at a given time
    def active(self, current_time):
        if self.completed:
            return False
        elif current_time < self.release:
            return False
        else:
            return True

    # advances progress on the task and checks for completion
    def advance(self, current_time):
        self.timeframes.append((current_time, 1))
        self.progress += 1
        if self.progress >= self.processing:
            self.complete(current_time + 1)

    # updates attributes to reflect task completion
    def complete(self, completed_time):
        self.completed = True
        if completed_time > self.deadline:
            self.late = completed_time - self.deadline
