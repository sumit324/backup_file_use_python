

import shutil
import os
import datetime

def backup_files(source_path, destination_path):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination_path, f"backup{today}")  # without extension
    shutil.make_archive(backup_file_name, 'gztar', source_path)  # tar.gz created automatically


# Use raw strings r'' or double slashes to avoid escape warning
source_path = r'Z:\Python_for_Devops'
destination_path = r'Z:\Python_for_Devops\backup'

backup_files(source_path, destination_path)
