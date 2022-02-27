import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import bangumiedit
app = QApplication(sys.argv)
window = QMainWindow()
ui = bangumiedit.Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())