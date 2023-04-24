import sys
# from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QComboBox, QHBoxLayout, QVBoxLayout, QLineEdit, QApplication
from PySide2.QtGui import *


class UploadUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # self.setWindowTitle("Upload Assets")
        # self.resize(700, 700)
        self.setWindowTitle("Upload Assets")
        self.setGeometry(700, 700, 700, 700)
        # self.set

        self.box_project = QComboBox()
        self.box_project.addItems(["1", "Project", "3"])
        self.box_project.setCurrentText("Project")

        self.box_task = QComboBox()
        self.box_task.addItems(["4", "5", "6"])

        self.box_asset = QComboBox()
        self.box_asset.addItems(["7", "8", "9"])

        box_layout = QHBoxLayout()
        box_layout.addWidget(self.box_project)
        box_layout.addWidget(self.box_task)
        box_layout.addWidget(self.box_asset)
        self.setLayout(box_layout)

        
        self.line_path = QLineEdit(self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.box_project)
        layout.addWidget(self.box_task)
        layout.addWidget(self.box_asset)
        layout.addWidget(self.line_path)
        self.setLayout(layout)

        # self.line_path.resize(400, 30)
        # self.line_path.move(50, 100)

def main():
    app = QApplication()
    uu = UploadUI()
    uu.show() 
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
