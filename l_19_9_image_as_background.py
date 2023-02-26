from PyQt6 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Изображение в качестве фона")
window.resize(500, 500)
pal = window.palette()
pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window, QtGui.QBrush(QtGui.QPixmap("bcgnd.png")))
window.setPalette(pal)
label = QtWidgets.QLabel()
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
label.setStyleSheet("background-image: url(Зубастик.ico);")
label.setAutoFillBackground(True)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())