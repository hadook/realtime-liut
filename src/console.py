from randomizer import Randomizer
from scheduler import Scheduler
from plotter import Plotter


# run task scheduler from console (without GUI)
def main():

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
