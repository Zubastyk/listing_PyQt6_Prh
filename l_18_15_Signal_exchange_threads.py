from PyQt6 import QtCore, QtWidgets

class Thread_1(QtCore.QThread):
    s1 = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.count = 0
    
    def run(self):
        self.exec()    # Запускается цикл обработки сигналов
    
    def on_start(self):
        print("Сработал on_start")
        print(self.count)
        self.count +=1
        print("self.count на выходе: ", self.count)
        self.s1.emit(self.count)
        
    
        
class Thread_2(QtCore.QThread):
    s2 = QtCore.pyqtSignal(str)
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.exec()    # Запускается цикл обработки сигналов
        
    def on_change(self, i):
        print("i на входе: ", i)
        print("Сработал on_change")
        i +=10
        print("i на выходе: ", i)
        self.s2.emit("%d" % i)
       
        
class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Нажмите кнопку")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.button = QtWidgets.QPushButton("Сгенерировать сигнал")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.thread_1 = Thread_1()
        self.thread_2 = Thread_2()
        self.thread_1.start() # Запускаем поток_1
        self.thread_2.start() # Запускаем поток_2
        self.button.clicked.connect(self.thread_1.on_start)
        print("Обработчик событий on_start")
        self.thread_1.s1.connect(self.thread_2.on_change)
        print("Обработчик событий on_change")
        self.thread_2.s2.connect(self.on_thread_2_s2)
        print("Обработчик событий on_thread_2_s2")
        
    def on_thread_2_s2(self, s):
        print("s: ", s)
        self.label.setText(s)
        print("Сработал on_thread_2_s2")
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Обмен сигналами мужду потоками")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec())
        