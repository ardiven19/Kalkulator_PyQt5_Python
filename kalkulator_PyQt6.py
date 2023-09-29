import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import math


class mainform(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setupUi()
        self._createmenubar()
    def _createmenubar(self):
        self.bar = QMenuBar()
        self.cal = self.bar.addMenu("kalkulator")

    def setupUi(self):
        self.tinggi = 650
        self.lebar = 500
        self.resize(self.lebar, self.tinggi)
        self.move(100, 100)
        self.setWindowTitle('kalkulator')
        self.setWindowIcon(QIcon('calculator.png'))
        self.setStyleSheet("background-color: #EF9595; font-size: 35px; font-family: 'Times New Roman', Times, serif;")

        self.tampilan = QLineEdit()
        self.tampilan.setFixedSize(int(self.lebar * 0.9), int(self.tinggi * 0.285))
        self.tampilan.setReadOnly(True)
        self.tampilan.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.tampilan.setStyleSheet(
            "background-color: darkseagreen; color: black; font-size: 30px; border: none; border-radius: 8px;")

        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7)  # Tingkat transparansi (0 hingga 1)

        # Menggunakan efek transparansi pada QLineEdit
        self.tampilan.setGraphicsEffect(opacity_effect)

        layout_tampilan = QHBoxLayout()
        layout_tampilan.addWidget(self.tampilan)

        layout_tombol = QGridLayout()
        listombol = [['sin', 'cos', 'tan', 'log'],
                     ['del', '(', ')', '**'],
                     ['7', '8', '9', '*'],
                     ['4', '5', '6', '/'],
                     ['1', '2', '3', '-'],
                     ['0', '.', '+', '=']]
        tampilantombol = [['sin', 'cos', 'tan', 'log'],
                          ['del', '(', ')', '^'],
                          ['7', '8', '9', 'x'],
                          ['4', '5', '6', '/'],
                          ['1', '2', '3', '-'],
                          ['0', '.', '+', '=']]
        tombollain = ['sin', 'cos', 'tan', 'log', 'del', '=', '**', '*']

        liststyle = [x for x in range(10)]

        for i in range(len(tampilantombol)):
            for j in range(len(tampilantombol[0])):
                tombol = listombol[i][j]
                tombolkalkulator = tampilantombol[i][j]
                self.button = QPushButton(tombolkalkulator)
                layout_tombol.addWidget(self.button, int(i), int(j))
                if tombol in str(liststyle):
                    self.button.setStyleSheet("background-color: #EBEF95; border: none; border-radius: 8px;")
                else:
                    self.button.setStyleSheet("background-color: #EFD595; border: none; border-radius: 8px;")
                self.button.setFixedSize(int(self.lebar * 0.2), int(self.tinggi * 0.114))

                self.button.clicked.connect(lambda checked, btn=tombol: self.klik_tombol(
                    btn, tombollain))

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_tampilan)
        layout_main.addLayout(layout_tombol)

        self.setLayout(layout_main)
        self.tampilan_list = []
        self.hitung = []

    def result(self):
        self.tampilan.clear()
        self.Result = str(eval(''.join(self.hitung)))

        # Menggunakan pembagian floor (//) untuk memastikan hasilnya adalah integer
        try:
            hasil_evaluasi = eval(''.join(str(x) for x in self.hitung))
            if hasil_evaluasi == int(hasil_evaluasi):
                self.Result = str(int(hasil_evaluasi))
            else:
                self.Result = str(hasil_evaluasi)
        except ZeroDivisionError:
            self.tampilan.setText('Division by zero error')
            return
        except Exception as e:
            self.tampilan.setText('Error')
            return

        if len(self.Result) > 22:
            self.tampilan.setText('EROR')
        else:
            self.tampilan.setText(self.Result)
            self.tampilan_list.clear()
            self.hitung.clear()
            self.tampilan_list.append(self.Result)
            self.hitung.append(self.Result)
    def updateTampilan(self):
        self.update = ''.join(self.tampilan_list)
        self.tampilan.setText(self.update)
    def tombollain(self, value):
        trigono = ['sin', 'cos', 'tan', 'log']
        if value == '=':
            self.result()  # Hapus hitung setelah hasil dihitung
        elif value == 'del':
            self.tampilan.clear()
            self.tampilan_list.clear()
            self.hitung.clear()
            self.hitung.clear()
        elif value == '**':
            self.tampilan_list.append('^')  # Gunakan '**' untuk operasi perpangkatan
            self.hitung.append('**')
            self.updateTampilan()
        elif value == '*':
            self.tampilan_list.append('x')
            self.hitung.append('*')
            self.updateTampilan()
        elif value in trigono:
            self.trigonometri(value)
    def klik_tombol(self, value, tombollain):
        if value in tombollain:
            self.tombollain(value)
        else:
            self.tampilan_list.append(value)
            self.hitung.append(value)
            self.updateTampilan()
    def trigonometri(self, value):

        self.tampilan_list.append(value+'(')
        self.hitung.append('math.'+value+'(')
        self.updateTampilan()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainform()
    main.show()
    sys.exit(app.exec())
