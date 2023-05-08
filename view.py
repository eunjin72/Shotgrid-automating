import sys

from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget, \
    QHBoxLayout, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QMessageBox


class AssetUploaderView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Upload Assets")
        self.resize(600, 200)
        self.center()

        # create widgets
        vb = QVBoxLayout()

        hbtop = QHBoxLayout()
        vb.addLayout(hbtop)
        self.com_project = QComboBox()
        self.com_asset = QComboBox()
        hbtop.addWidget(self.com_project)
        hbtop.addWidget(self.com_asset)

        hbmid = QHBoxLayout()
        vb.addLayout(hbmid)
        self.line_path = QLineEdit()
        self.btn_browse = QPushButton("Browse")
        hbmid.addWidget(self.line_path)
        hbmid.addWidget(self.btn_browse)

        hbbot = QHBoxLayout()
        vb.addLayout(hbbot)
        hbbot.addStretch()
        self.btn_upload = QPushButton("Upload")
        self.btn_cancel = QPushButton("cancel")
        hbbot.addWidget(self.btn_upload)
        hbbot.addWidget(self.btn_cancel)
        hbbot.addStretch()

        self.setLayout(vb)

        # button clicked event example
        self.btn_browse.clicked.connect(self.browse_test)
        self.btn_upload.clicked.connect(self.upload_test)
        self.btn_cancel.clicked.connect(self.cancel_test)

        self.show()

    def center(self):
        fg = self.frameGeometry()
        dw = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(dw)
        self.move(fg.topLeft())

    def message_box(self):
        msgbox = QMessageBox()
        msgbox.about(self, "Alert", "Complete")

    def browse_test(self):
        print("Select assets directory")

    def upload_test(self):
        self.message_box()
        print("Upload assets")

    def cancel_test(self):
        print("Close")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = AssetUploaderView()
    sys.exit(app.exec_())
