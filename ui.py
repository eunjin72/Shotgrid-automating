import sys

from PySide2.QtWidgets import QWidget, QComboBox, QHBoxLayout, QVBoxLayout, QLineEdit, QApplication, QPushButton, QFileDialog
from PySide2.QtGui import *


class UploadUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Upload Assets")
        self.setGeometry(200, 200, 600, 200)

        self.com_project = QComboBox()
        self.com_asset = QComboBox()
        self.line_path = QLineEdit()
        self.btn_browse = QPushButton("Browse")
        self.btn_ok = QPushButton("Ok")        
        self.btn_cancel = QPushButton("cancel")        

        self.vb = QVBoxLayout()
        self.hbTop = QHBoxLayout()
        self.hbMid = QHBoxLayout()
        self.hbBot = QHBoxLayout()
        self.vb.addLayout(self.hbTop)
        self.vb.addLayout(self.hbMid)
        self.vb.addLayout(self.hbBot)
        self.setLayout(self.vb)

        self.hbTop.addWidget(self.com_project)
        self.hbTop.addWidget(self.com_asset)

        self.hbMid.addWidget(self.line_path)
        self.hbMid.addWidget(self.btn_browse)

        self.hbBot.addStretch()
        self.hbBot.addWidget(self.btn_ok)
        self.hbBot.addWidget(self.btn_cancel)
        self.hbBot.addStretch()

        self.btn_browse.clicked.connect(self.get_asset_name)

        self.show()

    def get_asset_name(self):
        test = QFileDialog.getOpenFileName()
        print(test)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    uu = UploadUI()
    
    sys.exit(app.exec_())
    