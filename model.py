# from PySide2.QtWidgets import QFileDialog, QWidget

from shotgun_api3 import Shotgun
from pprint import pprint

SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = 'script_kej'
SCRIPT_KEY = 'kibjce#prQeimq3lsojkstgmq'

sg = Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


class Test():
    def __init__(self):
        pass
    
    def get_project(self):
        projects = sg.find("Project", filters=[["sg_status", "is", "Active"]], fields=["id", "name"])

        project = []
        for p in projects:
            project.append(p["name"])

        return project

    def get_asset_type(self):
        projects = sg.find("Project", filters=[["sg_status", "is", "Active"]], fields=["id", "name"])
        for p in projects:
            context = sg.schema_field_read('Asset', field_name="sg_asset_type", project_entity=p)
        return context["sg_asset_type"]["properties"]["valid_values"]["value"]
    
    # def get_asset_type(self):
    #     type = sg.find("Asset", filters=[["sg_asset_type", "is", "Active"]], fields=["id"])


    # def upload_asset(self):
    #     test_file = 'C:/Users/admin/Desktop/assets/Vehicle/car 001.fbx'
    #     sg.upload("Asset", 2402, test_file, field_name="sg_asset_type", display_name="car 001")    
    
    # def btn_cancel_clicked(self):
    #     self.close()

def main():
    t = Test()
    t.get_project()
    t.get_asset_type()
    # t.upload_assets()


if __name__ == "__main__":
    main()
