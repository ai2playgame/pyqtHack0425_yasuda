import sys
from PyQt5.QtWidgets import QApplication
from AiMainWidget import MainWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWidget()
    sys.exit(app.exec_())
