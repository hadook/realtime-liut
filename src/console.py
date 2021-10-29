# from task import Task
from randomizer import Randomizer
from scheduler import Scheduler
from plotter import Plotter


# run task scheduler from console (without GUI)
def main():

    # tasks = [Task(2, 4, 7), Task(1, 1, 2), Task(2, 0, 3), Task(1, 4, 5), Task(3, 2, 6)]
    tasks = Randomizer().tasks
    scheduler = Scheduler(tasks)
    scheduler.order_tasks()
    scheduler.print_tasks()
    scheduler.print_scheduling()
    scheduler.print_lateness()
    plotter = Plotter(scheduler.time, scheduler.tasks)
    plotter.draw()


if __name__ == '__main__':
    main()
