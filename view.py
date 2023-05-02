import sys

from PySide2.QtWidgets import QWidget, QComboBox, QHBoxLayout, QVBoxLayout, QLineEdit, QApplication, QPushButton


class AssetUploaderView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Upload Assets")
        self.setGeometry(200, 200, 600, 200)

        # create widgets
        self.com_project = QComboBox()
        self.com_asset = QComboBox()
        self.line_path = QLineEdit()
        self.btn_browse = QPushButton("Browse")
        self.btn_upload = QPushButton("Upload")        
        self.btn_cancel = QPushButton("cancel")        

        # layout
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
        self.hbBot.addWidget(self.btn_upload)
        self.hbBot.addWidget(self.btn_cancel)
        self.hbBot.addStretch()

        # button clicked event example
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.btn_upload.clicked.connect(self.btn_upload_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

        self.show()

    def btn_browse_clicked(self):
        print("Select assets directory")

    def btn_upload_clicked(self):
        print("Upload assets")

    def btn_cancel_clicked(self):
        print("Close")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui= AssetUploaderView()
    sys.exit(app.exec_())
    