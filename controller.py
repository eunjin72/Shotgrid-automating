import sys
from PySide2.QtWidgets import *

from view import AssetUploaderView
from model import AssetUploaderModel


class AssetUploaderController(AssetUploaderView):
    def __init__(self):
        super().__init__()
        self.model = AssetUploaderModel()

        # combobox event
        self.com_project.addItems(self.model.get_project_name())
        self.com_project.activated.connect(self.current_project)

        self.com_asset.addItems(self.model.get_asset_type())
        self.com_asset.activated.connect(self.current_asset_type)

        # button clicked event
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.btn_upload.clicked.connect(self.btn_upload_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

    def current_project(self):
        project = self.com_project.currentText()
        return project

    def current_asset_type(self):
        asset_type = self.com_asset.currentText()
        return asset_type
    
    def btn_browse_clicked(self):
        dialog = QFileDialog()
        dialog.setDirectory(r'C:\shotgrid')
        self.dir_path = dialog.getExistingDirectory()
        self.line_path.setText(self.dir_path)

    def btn_upload_clicked(self):
        self.model.upload_assets(self.current_project(), self.dir_path, self.current_asset_type())
        self.message_box()
        
    def btn_cancel_clicked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    auc = AssetUploaderController()
    sys.exit(app.exec_())
