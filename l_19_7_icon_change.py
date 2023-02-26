from PyQt6 import QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Смена значка окна")
window.resize(300, 100)
ico = QtGui.QIcon(r"зуб16.png")
#ico = window.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
window.setWindowIcon(ico)
app.setWindowIcon(ico)
window.show()
sys.exit(app.exec())