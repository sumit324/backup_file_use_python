import shutil
import os

def practice(source,destination):
    practice_file = os.path.join(destination,"backup_file")
    shutil.make_archive(practice_file,'gztar',source)

source = r'Z:\Python_for_Devops'
destination = r'Z:\Python_for_Devops\demo'

practice(source,destination)
