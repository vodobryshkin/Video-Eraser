import sys

from PyQt5.QtWidgets import QApplication

from py_pages.py_start_page import StartForm
from py_pages.py_main_page import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    st = StartForm()
    mn = MainWindow()

    if not st.complete:
        st.show()
    else:
        mn.show()

    sys.exit(app.exec_())
