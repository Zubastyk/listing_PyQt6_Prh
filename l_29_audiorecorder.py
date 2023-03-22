from PyQt6 import QtCore, QtWidgets, QtMultimedia
import sys, os


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, 
                                   flags=QtCore.Qt.WindowType.Window |
                                   QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Запись звука")
        # Создаем транспорт, звуковой вход и кодировщик
        mcs = QtMultimedia.QMediaCaptureSession(parent=self)
        self.aInput = QtMultimedia.QAudioInput(parent=self)
        self.aInput.setVolume(1.0)
        mcs.setAudioInput(self.aInput)
        self.ardRecorder = QtMultimedia.QMediaRecorder(parent=self)
        # Звук будет сохраняться в файле record.mp3, находящемся
        # в той же папке, где хранится прграмма
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("record.mp3"))
        self.ardRecorder.setOutputLocation(fn)
        # Указываем формат файла MP3
        mf = QtMultimedia.QMediaFormat(
            QtMultimedia.QMediaFormat.FileFormat.MP3)
        mf.setAudioCodec(QtMultimedia.QMediaFormat.AudioCodec.MP3)
        self.ardRecorder.setMediaFormat(mf)
        # Задаем параметры кодирования звука
        self.ardRecorder.setQuality(
            QtMultimedia.QMediaRecorder.Quality.LowQuality)
        self.ardRecorder.setEncodingMode(
            QtMultimedia.QMediaRecorder.EncodingMode.ConstantQualityEncoding)
        self.ardRecorder.setAudioChannelCount(1)
        self.ardRecorder.setAudioSampleRate(-1)
        self.ardRecorder.recorderStateChanged.connect(self.initRecorder)
        self.ardRecorder.durationChanged.connect(self.showDuration)
        # Создаем компоненты для запуска, приостановки и остановки
        # записи звука и регулировани его уровня
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        self.btnRecord = QtWidgets.QPushButton("&Запись")
        self.btnRecord.clicked.connect(self.ardRecorder.record)
        hbox.addWidget(self.btnRecord)
        self.btnPause = QtWidgets.QPushButton("П&ауза")
        self.btnPause.clicked.connect(self.ardRecorder.pause)
        self.btnPause.setEnabled(False)
        hbox.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton("&Стоп")
        self.btnStop.clicked.connect(self.ardRecorder.stop)
        self.btnStop.setEnabled(False)
        hbox.addWidget(self.btnStop)
        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel("&Уровень записи")
        hbox.addWidget(lblVolume)
        self.sldVolume = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.sldVolume.setRange(0, 100)
        self.sldVolume.setTickPosition(
            QtWidgets.QSlider.TickPosition.TicksAbove)
        self.sldVolume.setTickInterval(10)
        self.sldVolume.setValue(100)
        lblVolume.setBuddy(self.sldVolume)
        self.sldVolume.valueChanged.connect(self.setVolume)
        hbox.addWidget(self.sldVolume)
        vbox.addLayout(hbox)
        # Создаем надпись, в которую будет выводиться состояние программы
        self.lblStatus = QtWidgets.QLabel("Готово")
        vbox.addWidget(self.lblStatus)
        self.setLayout(vbox)
        self.resize(300, 100)
    # В зависимости от состояния записи звука делаем нужные    
    # кнопки доступными или, напротив, недоступными и выводим
    # соотвкетствующий текст надписи
    def initRecorder(self, state):
        match state:
            case QtMultimedia.QMediaRecorder.RecorderState.RecordingState:
                print("rec")
                self.btnRecord.setEnabled(False)
                self.btnPause.setEnabled(True)
                self.btnStop.setEnabled(True)
                self.lblStatus.setText("Запись")
            case QtMultimedia.QMediaRecorder.RecorderState.PausedState:
                self.btnRecord.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.lblStatus.setText("Пауза")
            case QtMultimedia.QMediaRecorder.RecorderState.StoppedState:
                self.btnRecord.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(False)
                self.lblStatus.setText("Готово")      
    
    # Выводим продолжительность записанного звука
    def showDuration(self, duration):
        print("duration")
        self.lblStatus.setText("Записано" + str(duration//1000)+ "секунд")  
    
    
    def setVolume(self, value):
        print("Volume")
        self.aInput.setVolume(value / 100)
        
    # При закрытии окна останавливаем запись
    def closeEvent(self, e):
        self.ardRecorder.stop()
        e.accept()
        QtWidgets.QWidget.closeEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec()) 
        
    
    
        
        
        