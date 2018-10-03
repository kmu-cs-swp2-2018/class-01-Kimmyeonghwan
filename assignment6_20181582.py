import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        # 인터페이스
        # 버튼
        self.Add = QPushButton("Add", self)
        # self.Add.move(70, 70)
        self.Del = QPushButton("Del", self)
        # self.Del.move(155, 70)
        self.Find = QPushButton("Find", self)
        # self.Find.move(240, 70)
        self.Inc = QPushButton("Inc", self)
        # self.Inc.move(325, 70)
        self.Show = QPushButton("Show", self)
        # self.Show.move(410, 70)

        # 라벨
        Name_label = QLabel("Name:", self)
        # Name_label.move(20,10)
        self.Name_text = QLineEdit("", self)
        # self.Name_text.move(60,10)

        Age_label = QLabel("Age:", self)
        # Age_label.move(180, 10)
        self.Age_text = QLineEdit("", self)
        # self.Age_text.move(220, 10)

        Score_label = QLabel("Score:", self)
        # Score_label.move(340, 10)
        self.Score_text = QLineEdit("", self)
        # self.Score_text.move(380, 10)

        self.Amount_label = QLabel("Amount:", self)
        # self.Amount_label.move(200, 40)
        self.Amount_text = QLineEdit("", self)
        # self.Amount_text.move(255, 40)

        Key_label = QLabel("Key:", self)
        # Key_label.move(370, 40)
        self.Key_select = QComboBox(self)
        self.Key_select.addItems(["Name", "Age", "Score"])
        # self.Key_select.move(400,40)

        # Result
        Result_label = QLabel("Result:", self)
        # Result_label.move(20, 100)
        self.Result_text = QTextEdit(self)
        # Result_text.move(70, 100)

        # 레이아웃
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(Name_label)
        hbox.addWidget(self.Name_text)
        hbox.addWidget(Age_label)
        hbox.addWidget(self.Age_text)
        hbox.addWidget(Score_label)
        hbox.addWidget(self.Score_text)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.Amount_label)
        hbox2.addWidget(self.Amount_text)
        hbox2.addWidget(Key_label)
        hbox2.addWidget(self.Key_select)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.Add)
        hbox3.addWidget(self.Del)
        hbox3.addWidget(self.Find)
        hbox3.addWidget(self.Inc)
        hbox3.addWidget(self.Show)
        vbox.addLayout(hbox3)

        vbox2 = QVBoxLayout()
        hbox4 = QHBoxLayout()
        vbox2.addWidget(Result_label)
        hbox4.addLayout(vbox2)
        hbox4.addStretch(1)
        vbox.addLayout(hbox4)
        vbox.addWidget(self.Result_text)

        # 버튼 클릭 이벤트 신호 보냄
        self.Add.clicked.connect(self.doScoreDB_Add)
        self.Del.clicked.connect(self.doScoreDB_Del)
        self.Find.clicked.connect(self.doScoreDB_Find)
        self.Inc.clicked.connect(self.doScoreDB_Inc)
        self.Show.clicked.connect(self.doScoreDB_Show)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

        # Add 버튼을 눌렀을 때 이벤트 신호 받음.

    def doScoreDB_Add(self):
        record = {'Name': self.Name_text.text(), 'Age': int(self.Age_text.text()), 'Score': int(self.Score_text.text())}
        self.scoredb += [record]
        for dic in self.scoredb:
            dic['Age'] = int(dic['Age'])
            dic['Score'] = int(dic['Score'])
        self.showScoreDB()

        # Del 버튼을 눌렀을 때 이벤트 신호 받음.

    def doScoreDB_Del(self):
        for dic in self.scoredb:
            if dic['Name'] == self.Name_text.text():
                self.scoredb.remove(dic)
        self.showScoreDB()

        # Find 버튼을 눌렀을 때 이벤트 신호 받음.

    def doScoreDB_Find(self):
        out = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.Key_select.currentText()]):
            if p["Name"] == self.Name_text.text():
                for attr in sorted(p):
                    out += attr + "=" + str(p[attr]) + " "
                out += "\n"
        self.Result_text.setText(out)

        # Inc 버튼을 눌렀을 때 이벤트 신호 받음.

    def doScoreDB_Inc(self):
        for dic in self.scoredb:
            if dic['Name'] == self.Name_text.text():
                dic['Score'] = int(dic['Score'])
                dic['Score'] += int(self.Amount_text.text())
        self.showScoreDB()

        # Show 버튼을 눌렀을 때 이벤트 신호 받음.

    def doScoreDB_Show(self):
        out = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.Key_select.currentText()]):
            p['Age'] = int(p['Age'])
            p['Score'] = int(p['Score'])
            for attr in sorted(p):
                out += attr + "=" + str(p[attr]) + " "
            out += "\n"
        self.Result_text.setText(out)

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    # show 버튼과 다르게, 정렬 값이 아닌, 그대로의 값을 출력.
    def showScoreDB(self):
        out = ""
        for p in self.scoredb:
            for attr in sorted(p):
                out += attr + "=" + str(p[attr]) + " "
            out += "\n"
        self.Result_text.setText(out)
        print()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
