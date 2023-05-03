import sys

from PySide2.QtWidgets import QWidget, QComboBox, QHBoxLayout, QVBoxLayout, QLineEdit, QApplication, QPushButton


class AssetUploaderView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Upload Assets")
        #self.resize( 600, 200 )
        self.setGeometry(200, 200, 600, 200)

        # create widgets
        self.com_project = QComboBox()
        self.com_asset = QComboBox()
        self.line_path = QLineEdit()
        self.btn_browse = QPushButton("Browse")
        self.btn_upload = QPushButton("Upload")        
        self.btn_cancel = QPushButton("cancel")        

        # layout
        vb = QVBoxLayout()
        hbTop = QHBoxLayout()
        hbMid = QHBoxLayout()
        hbBot = QHBoxLayout()
        vb.addLayout(hbTop)
        vb.addLayout(hbMid)
        vb.addLayout(hbBot)

        hbTop.addWidget(self.com_project)
        hbTop.addWidget(self.com_asset)

        hbMid.addWidget(self.line_path)
        hbMid.addWidget(self.btn_browse)

        hbBot.addStretch()
        hbBot.addWidget(self.btn_upload)
        hbBot.addWidget(self.btn_cancel)
        hbBot.addStretch()

        self.setLayout(vb)

        # button clicked event example
        self.btn_browse.clicked.connect(self.btn_browse_test)
        self.btn_upload.clicked.connect(self.btn_upload_test)
        self.btn_cancel.clicked.connect(self.btn_cancel_test)

        self.show()

    def btn_browse_test(self):
        print("Select assets directory")

    def btn_upload_test(self):
        print("Upload assets")

    def btn_cancel_test(self):
        print("Close")


# if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ui= AssetUploaderView()
    # sys.exit(app.exec_())
    