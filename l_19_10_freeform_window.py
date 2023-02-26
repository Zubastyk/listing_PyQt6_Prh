from PyQt6 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.WindowType.Window | 
                      QtCore.Qt.WindowType.FramelessWindowHint)
window.setWindowTitle("Создание окна произвольной формы")
window.resize(600, 600)
pixmap = QtGui.QPixmap("Зубастик.png")
pal = window.palette()
pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window, 
             QtGui.QBrush(pixmap))
pal.setBrush(QtGui.QPalette.ColorGroup.Inactive,
             QtGui.QPalette.ColorRole.Window, QtGui.QBrush(pixmap))
window.setPalette(pal)
window.setMask(pixmap.mask())
button = QtWidgets.QPushButton("Закрыть окно", window)
button.setFixedSize(150,30)
button.move(175, 235)
button.clicked.connect(QtWidgets.QApplication.instance().quit)
window.show()
sys.exit(app.exec())
