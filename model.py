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
        projects = sg.find("Project", filters=[["sg_status", "is", "Active"]], fields=["name"])
        return projects

    def get_asset_type(self):
        for p in self.get_project():
            context = sg.schema_field_read('Asset', field_name="sg_asset_type", project_entity=p)
            pprint(context["sg_asset_type"]["properties"]["valid_values"]["value"])

def main():
    t = Test()
    t.get_project()
    t.get_asset_type()


if __name__ == "__main__":
    main()
