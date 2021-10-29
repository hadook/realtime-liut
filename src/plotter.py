import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class Plotter:
    """ Class for creating the Gantt diagram """

    def __init__(self, time, tasks):
        self.time = time
        self.tasks = list(reversed(tasks))

    def draw(self):
        fig, ax = plt.subplots()

        for i, task in enumerate(self.tasks):
            ax.broken_barh(task.timeframes, (i, 1), facecolors=task.color)

        ax.set_xlim(0, self.time)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlabel('time units')
        ax.set_ylim(0, len(self.tasks))
        ax.set_yticks(self.get_yticks())
        ax.set_yticklabels(self.get_labels())
        ax.grid(b=True, axis='x')
        ax.grid(b=True, axis='y', color='lightgreen', linestyle='--', linewidth=0.2)
        plt.show()

    def get_xticks(self):
        ticks = []
        for i in range(0, self.time + 1):
            ticks.append(i)
        return ticks

    def get_yticks(self):
        ticks = []
        for i, task in enumerate(self.tasks):
            ticks.append(i + 0.5)
        return ticks

    def get_labels(self):
        labels = []
        for task in self.tasks:
            labels.append(task.name)
        return labels
