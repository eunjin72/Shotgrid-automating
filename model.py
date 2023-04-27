import os

from shotgun_api3 import Shotgun
from pprint import pprint


# Shotgrid Api connect
SERVER_PATH = "https://rndtest.shotgrid.autodesk.com"
SCRIPT_NAME = 'script_kej'
SCRIPT_KEY = 'kibjce#prQeimq3lsojkstgmq'
sg = Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


class AssetUploaderModel():
    def __init__(self):
        self.projects = sg.find("Project", filters=[["sg_status", "is", "Active"]], fields=["id", "name"])

    
    def get_project_name(self):
        project_name = []
        for p in self.projects:
            project_name.append(p["name"])
        return project_name

    def get_asset_type(self):
        for p in self.projects:
            context = sg.schema_field_read('Asset', field_name="sg_asset_type", project_entity=p)
        return context["sg_asset_type"]["properties"]["valid_values"]["value"]
    
    def upload_assets(self, project_name, asset_dir_path, asset_type):
        project = sg.find_one("Project", filters=[["name", "is", project_name]])

        asset_lists = os.listdir(asset_dir_path)
        asset_list = []
        for l in asset_lists:
            asset_list.append(os.path.splitext(l)[0])
            for asset_name in asset_list:
                data = {
                    'project': {"type":"Project", "id": project["id"]},
                    'code': asset_name,
                    'sg_asset_type': asset_type
                    }     
            
            result = sg.create('Asset', data)
        
        pprint(result)


def main():
    model = AssetUploaderModel()
    model.get_project_name()
    model.get_asset_type()
    model.upload_assets(
        project_name=input("Enter the Project Name : "), 
        asset_dir_path=input("Enter the path of Assets : "), 
        asset_type=input("Enter the Asset type : "))
    

if __name__ == "__main__":
    main()
