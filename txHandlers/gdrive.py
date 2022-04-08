import json
import requests
from global_app_data import GlobalAppData


# Class to upload input file onto the google drive.
# Access token can be generated from https://developers.google.com/oauthplayground
# And is expected to be input based upon the user gmail id.
class Gdrive:
    @staticmethod
    def upload_file_to_drive(access_token, file_name_with_path, parent_dir, upload_file_name, event):
        print("Upload file to drive")
        headers = {"Authorization": "Bearer "+access_token}

        if 0 == len(parent_dir):
            para = {
                "name": upload_file_name
            }
        else:
            para = {
                "name": upload_file_name,
                "parents": [parent_dir]
            }

        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': ('application/text', open(file_name_with_path, "rb"))
        }

        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files,
            verify=False
        )

        print ("Gdrive:Upload file access token", access_token, "\n file path with name",
               file_name_with_path, "\n uploaded file name", upload_file_name)
        print(headers, "--", files, "--", para)
        #import time
        #time.sleep(0.3)
        GlobalAppData.set_g_drive_file_upload_result(r.text)
        print(r.text)
        event.set()