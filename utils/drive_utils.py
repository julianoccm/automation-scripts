import shutil
from config.scripts_configurations import PATH_GOOGLE_DRIVE

def upload_file_google_drive(file):
    shutil.copy(file, PATH_GOOGLE_DRIVE)