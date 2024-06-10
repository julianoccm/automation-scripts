import sys
import utils.drive_utils
import utils.compacter_utils
from datetime import datetime
from utils.config.scripts_configurations import PATH_TEMP, PATH_FOLDER_TO_BACKUP, BACKUP_FILE_NAME_TEMPLATE

def backup_workspace():
    current_year = str(datetime.now().year)
    current_month = str(datetime.now().month)
    current_day = str(datetime.now().day)

    file_name = f"{PATH_TEMP}\{BACKUP_FILE_NAME_TEMPLATE}"
    file_name = str.replace(file_name, "YYYY", current_year)
    file_name = str.replace(file_name, "MM", current_month)
    file_name = str.replace(file_name, "DD", current_day)

    zipped_file_name = file_name + ".zip"

    utils.compacter_utils.zip_directory(filename=file_name, target_dir=PATH_FOLDER_TO_BACKUP)
    utils.drive_utils.upload_file_google_drive(zipped_file_name)

if __name__ == "__main__":
    backup_workspace()
    sys.exit()