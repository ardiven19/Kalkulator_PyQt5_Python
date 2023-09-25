import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMenuBar
class mainform(QWidget):


    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):


        self.tinggi = 600
        self.lebar = 450
        self.resize(self.lebar, self.tinggi)
        self.move(100, 100)
        self.setWindowTitle('kalkulator')
        self.setWindowIcon(QIcon('E:/Aplikasi/ICCon/LOGO/black-spider.ico'))
        self.setStyleSheet("background-color: indigo; font-size: 30px; font-family: 'Times New Roman', Times, serif;")

        self.tampilan = QLineEdit()
        self.tampilan.setFixedSize(int (self.lebar * 0.9), int(self.tinggi * 0.285))
        self.tampilan.setReadOnly(True)
        self.tampilan.setStyleSheet("background-color: darkseagreen; color: black; font-size: 30px; border: none; border-radius: 8px;")

        layout_tampilan = QHBoxLayout()
        layout_tampilan.addWidget(self.tampilan)

        
        layout_tombol = QGridLayout()
        listombol = [['del', '(', ')', '**'],
                     ['7', '8', '9', '*'], 
                     ['4', '5', '6', '/'],
                     ['1', '2', '3', '-'],
                     ['0', '.', '+', '=']]
        tampilantombol = [['del', '(', ')', '^'],
                          ['7', '8', '9', 'x'], 
                          ['4', '5', '6', '/'],
                          ['1', '2', '3', '-'],
                          ['0', '.', '+', '=']]
        
        liststyle = [x for x in range(10)]
        
        for i in range(5):
            for j in range(4):
                tombol = listombol[i][j]
                tombolkalkulator = tampilantombol[i][j] 
                self.button = QPushButton(tombolkalkulator)
                layout_tombol.addWidget(self.button, int(i), int(j))
                if tombol in str(liststyle):
                    self.button.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
                else:
                    self.button.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;") 
                self.button.setFixedSize(int(self.lebar * 0.2), int(self.tinggi * 0.114))

                self.button.clicked.connect(lambda checked, btn = tombol: self.klik_tombol(btn) if btn != 'del' and btn!='=' and btn!='**' else self.tombollain(btn))

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
            hasil_evaluasi = eval(''.join(self.hitung))
            # Memeriksa apakah hasil memiliki angka di belakang koma
            if hasil_evaluasi == int(hasil_evaluasi):
                self.Result = str(int(hasil_evaluasi))  # Jika tidak ada angka di belakang koma, jadikan integer
            else:
                self.Result = str(hasil_evaluasi)  # Jika ada angka di belakang koma, biarkan sebagai float
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
        if value == '=':
            self.result()        # Hapus hitung setelah hasil dihitung
        elif value == 'del':
            self.tampilan.clear()
            self.tampilan_list.clear()
            self.hitung.clear()
            self.hitung.clear()
        elif value == '**':
            self.tampilan_list.append('^')# Gunakan '**' untuk operasi perpangkatan
            self.hitung.append('**')
            self.updateTampilan()
    def klik_tombol(self, value):

        self.tampilan_list.append(value)
        self.hitung.append(value)
        self.updateTampilan()



if __name__=='__main__':
    app = QApplication(sys.argv)
    main = mainform()
    main.show()
    app.exec_()
