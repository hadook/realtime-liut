from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from task import Task
from randomizer import Randomizer
from scheduler import Scheduler
from plotter import Plotter


# represents the main application window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("../gui/win_main.ui", self)
        self.tasks = []
        self.output = ""
        self.format_table()
        self.connect_buttons()

    def format_table(self):
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        for i in range(0, 4):
            self.table.setColumnWidth(i, 30)

    def connect_buttons(self):
        self.btn_randomize.clicked.connect(self.randomize_tasks)
        self.btn_clear.clicked.connect(self.clear_tasks)
        self.btn_add.clicked.connect(self.add_task)
        self.btn_edit.clicked.connect(self.edit_task)
        self.btn_delete.clicked.connect(self.delete_task)
        self.btn_schedule.clicked.connect(self.run_scheduler)

    def update_tasks(self):
        self.tasks = []
        Task.num_tasks = 0
        for i in range(0, self.table.rowCount()):
            p = int(self.table.item(i, 1).text())
            r = int(self.table.item(i, 2).text())
            d = int(self.table.item(i, 3).text())
            self.tasks.append(Task(p, r, d))

    def clear_tasks(self):
        Task.num_tasks = 0
        self.tasks = []
        self.output = ""
        self.table.setRowCount(0)
        self.console.setPlainText("")

    def randomize_tasks(self):
        self.clear_tasks()
        tasks = Randomizer().tasks
        self.table.setRowCount(len(tasks))
        for i, task in enumerate(tasks):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(task.name)))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(task.processing)))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(task.release)))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(task.deadline)))
            for j in range(0, 4):
                self.table.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

    def add_task(self):
        dialog = TaskWindow(False)
        if dialog.exec_():
            i = self.table.rowCount()
            self.table.setRowCount(i + 1)
            task = Task(dialog.p, dialog.r, dialog.d)
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(task.name)))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(task.processing)))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(task.release)))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(task.deadline)))
            for j in range(0, 4):
                self.table.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

    def edit_task(self):
        i = self.table.currentRow()
        if i == -1:
            self.output = "No task selected."
            self.print_output()
        else:
            p = int(self.table.item(i, 1).text())
            r = int(self.table.item(i, 2).text())
            d = int(self.table.item(i, 3).text())
            dialog = TaskWindow(True, p, r, d)
            if dialog.exec_():
                self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(dialog.p)))
                self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dialog.r)))
                self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(dialog.d)))
                for j in range(0, 4):
                    self.table.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

    def delete_task(self):
        i = self.table.currentRow()
        if i == -1:
            self.output = "No task selected."
            self.print_output()
        else:
            Task.num_tasks -= 1
            self.table.removeRow(i)
            for i in range(0, self.table.rowCount()):
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem("Z" + str(i+1)))
                self.table.item(i,0).setTextAlignment(QtCore.Qt.AlignCenter)

    def run_scheduler(self):
        self.output = ""
        self.update_tasks()
        if len(self.tasks) == 0:
            self.output = "No tasks configured."
            self.print_output()
        else:
            scheduler = Scheduler(self.tasks)
            scheduler.order_tasks()
            self.output += scheduler.str_scheduling()
            self.output += "\n" + scheduler.str_lateness()
            self.print_output()
            plotter = Plotter(scheduler.time, scheduler.tasks)
            plotter.draw()

    def print_output(self):
        self.console.setPlainText(self.output)


# represents dialog window to configure a task
class TaskWindow(QDialog):

    def __init__(self, edit, p=None, r=None, d=None):
        super(TaskWindow, self).__init__()
        uic.loadUi("../gui/win_task.ui", self)
        self.edit = edit
        self.p = p
        self.r = r
        self.d = d
        self.v = QIntValidator(0, 99, self)
        self.setup_inputs()
        self.connect_buttons()

    def setup_inputs(self):
        inputs = [self.lineEdit_p, self.lineEdit_r, self.lineEdit_d]
        for item in inputs:
            item.setMaxLength(2)
            item.setValidator(self.v)
        if self.edit:
            self.lineEdit_p.setText(str(self.p))
            self.lineEdit_r.setText(str(self.r))
            self.lineEdit_d.setText(str(self.d))

    def connect_buttons(self):
        self.btn_ok.clicked.connect(self.click_ok)
        self.btn_cancel.clicked.connect(self.click_cancel)

    def click_ok(self):
        self.p = self.get_int(self.lineEdit_p.text())
        self.r = self.get_int(self.lineEdit_r.text())
        self.d = self.get_int(self.lineEdit_d.text())
        # exceptions
        if self.p == 0:
            self.lineEdit_p.setText(str(1))
        elif self.d < self.r + self.p:
            self.lineEdit_d.setText(str(self.r + self.p))
        else:
            self.accept()

    def click_cancel(self):
        self.reject()

    @staticmethod
    def get_int(text):
        if text == "":
            return 0
        else:
            return int(text)
