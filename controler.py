import sys
from PySide2.QtWidgets import QWidget, QApplication

from ui import AssetUploaderView
from model import AssetUploaderModel


class AssetUploaderControler(QWidget):
    def __init__(self):
        super().__init__()
        self.model = AssetUploaderModel()
        self.view = AssetUploaderView()

        # 따로 test
        self.view.com_project.addItems(self.model.get_project_name())
        self.view.com_asset.addItems(self.model.get_asset_type())

        self.view.com_project.activated.connect(self.current_project)
        self.view.com_asset.activated.connect(self.current_asset_type)


        self.view.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.view.btn_upload.clicked.connect(self.btn_upload_clicked)
        self.view.btn_cancel.clicked.connect(self.btn_cancel_clicked)
    


    def current_project(self):
        project = self.view.com_project.currentText()
        return project

    def current_asset_type(self):
        asset_type = self.view.com_asset.currentText()
        return asset_type
    
    def btn_browse_clicked(self):
        self.close()

    def btn_upload_clicked(self):
        self.close()
        
    def btn_cancel_clicked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    AssetUploaderControler()

    sys.exit(app.exec_())





##test

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

    # def set_project(self):
        # temps = self.model.get_project() 
        # temp = []
        # for t in temps[1]:
        #     temp.append(t)

        # print(temp)
        # return temp["name"]