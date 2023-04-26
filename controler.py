import sys
from PySide2.QtWidgets import QWidget, QApplication

from ui import UploadUI
from model import Test

from shotgun_api3 import Shotgun
from pprint import pprint

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = 'script_kej'
SCRIPT_KEY = 'kibjce#prQeimq3lsojkstgmq'

sg = Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


class ControlTest(QWidget):
    def __init__(self):
        super().__init__()
        self.model = Test()
        self.view = UploadUI()

        # 따로 test
        self.view.com_project.addItem(self.set_project()) 
        self.view.com_asset.addItems(self.model.get_asset_type())

        self.view.com_project.activated.connect(self.current_project)
        self.view.com_asset.activated.connect(self.current_asset_type)

        self.view.btn_ok.clicked.connect(self.upload_assets)
        # self.view.btn_browse.clicked.connect(self.model.get_dir_path)
        self.view.btn_cancel.clicked.connect(self.btn_cancel_clicked)


        # 연동 test
        # aa = self.model.get_project()
        # bb = self.model.get_asset_type()
        # for a in aa:
        #     self.view.com_project.addItem(a, bb)
        # # self.view.com_project.addItem("IL", ["123", "456", "789"])

        # self.view.com_project.currentIndexChanged.connect(self.update)
        # self.update(self.view.com_project.currentIndex())

    # 연동 test
    # def update(self, index):
    #     self.view.com_asset.clear()
    #     type = self.view.com_project.itemData(index)
    #     if type:
    #         self.view.com_asset.addItems(type)

    def set_project(self):
        # temp = []
        temp = self.model.get_project()
        print(temp)
        # return temp["name"]

    def current_project(self):
        project = self.view.com_project.currentText()
        return project

    def current_asset_type(self):
        type = self.view.com_asset.currentText()
        return type

    def upload_assets(self):
        data = {
            'project': {"type":"Project", "name": self.current_project()},
            'code': 'dino 003', # file name
            'sg_asset_type': self.current_asset_type() #type_name
            }
        result = sg.create('Asset', data)
        print(result)
    
    def btn_cancel_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ct = ControlTest()

    sys.exit(app.exec_())
