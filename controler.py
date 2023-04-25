import sys
from PySide2.QtWidgets import QWidget, QApplication

from ui import UploadUI
from model import Test


class ControlTest(QWidget):
    def __init__(self):
        super().__init__()
        self.view = UploadUI()
        self.view.com_project.addItems(["1", "Project", "3"])
        self.view.box_project.setCurrentText("Project")

    
    # def set_com_project(self):
    #     return ["1", "Project", "3"]


    def set_com_asset_type(self):
        pass

    def get_dir_path(self):
        pass

    def upload_asset(self):
        # mov_file = '/data/show/ne2/100_110/anim/01.mlk-02b.mov'
        # sg.upload("Shot", 423, mov_file, field_name="sg_latest_quicktime", display_name="Latest QT")
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    uu = UploadUI()
    # dm.show()
    # du = DownloadUI()
    # du.show()

    sys.exit(app.exec_())
