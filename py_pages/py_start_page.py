import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

from py_designes.py_start_page_design import Ui_StartForm
from py_pages.py_main_page import MainWindow


class StartForm(QWidget, Ui_StartForm):
    def __init__(self):
        super().__init__()

        self.complete = int(open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='r').readlines()[-1])
        print(self.complete)

        self.setupUi(self)

        self.lead_class = MainWindow()

        self.ok_button.clicked.connect(self.ok_button_function)
        self.tool_button.clicked.connect(self.tool_button_function)
        self.do_not_show_radio_button.clicked.connect(self.do_not_show_radio_button_function)

        file = open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='r').readlines()[0]

        if file != 'NONE\n' and file[0] != '\n':
            self.file_name_label.setText(file)

    def ok_button_function(self):
        file = open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='r').readlines()

        if file[0] == 'NONE\n' or file[0] == '\n':
            self.show_error_label.setText('Директория для сохранения не выбрана.')
        else:
            self.complete = 1
            self.lead_class.show()
            self.hide()

    def tool_button_function(self):
        way = QFileDialog.getExistingDirectory(self, "Выберите путь", "C:\\Users\\")

        if way == '':
            way = 'NONE\n'

        old_file = open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='r').readlines()
        old_s = old_file[1]

        file = open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='w')
        file.write(way + '\n')
        file.write(old_s)

        self.file_name_label.setText(way)

    def do_not_show_radio_button_function(self):
        old_file = open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='r').readlines()
        old_s = old_file[0]

        file = open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='w')
        file.write(old_s)

        if self.do_not_show_radio_button.isChecked():
            file.write('1\n')
        else:
            file.write('0\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartForm()
    ex.show()

    sys.exit(app.exec_())
