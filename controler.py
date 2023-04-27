import sys
from PySide2.QtWidgets import QWidget, QApplication, QFileDialog

from view import AssetUploaderView
from model import AssetUploaderModel


class AssetUploaderControler(QWidget):
    def __init__(self):
        super().__init__()
        self.model = AssetUploaderModel()
        self.view = AssetUploaderView()

        # combobox event
        self.view.com_project.addItems(self.model.get_project_name())
        self.view.com_project.activated.connect(self.current_project)

        self.view.com_asset.addItems(self.model.get_asset_type())
        self.view.com_asset.activated.connect(self.current_asset_type)

        # button clicked event
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
        self.dir_path= QFileDialog.getExistingDirectory()
        self.view.line_path.setText(self.dir_path)

    def btn_upload_clicked(self):
        self.model.upload_assets(self.current_project(), self.dir_path, self.current_asset_type())
        
    def btn_cancel_clicked(self):
        self.view.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    auc = AssetUploaderControler()
    sys.exit(app.exec_())
