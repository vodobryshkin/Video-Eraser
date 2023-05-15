import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from py_designes.py_main_page_design import Ui_MainWindow
from scripts.main_script import main_script


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.chosen_dict_file = ''
        self.phrase = ''
        self.file = ''
        self.new_file = ''

        self.setupUi(self)

        self.ok_button.clicked.connect(self.ok_button_function)

        self.tool_button1.clicked.connect(self.tool_button1_function)
        self.tool_button2.clicked.connect(self.tool_button2_function)

    def ok_button_function(self):
        self.phrase = self.phrase_text_edit.toPlainText()
        self.new_file = self.file_line_edit.text()

        path = open(os.getcwd() + '\\tools\\tools.txt', encoding='utf-8', mode='r').readlines()[0]

        try:
            self.result_label.setText(
                main_script(self.chosen_dict_file, self.phrase, self.file, path[:-1] + '/' + self.new_file))
        except Exception as error:
            self.result_label.setText(f'{error}')
            print(error)

    def tool_button2_function(self):
        self.file = QFileDialog.getOpenFileName(self, "Выберите файл", "C:\\Users\\")[0]
        self.chose_film_label.setText('Файл: ' + self.file.split('/')[-1])

    def tool_button1_function(self):
        self.chosen_dict_file = QFileDialog.getOpenFileName(self, "Выберите файл", "C:\\Users\\")[0]
        self.dict_label.setText('Словарь: ' + self.chosen_dict_file.split('/')[-1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
