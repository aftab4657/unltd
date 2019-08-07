import datetime

from django.core.files.storage import FileSystemStorage
from django.db import connection

from UNLTDjango.settings import DB_ROOT
from unltd.models import Backup
import time,os


class Unltdbackup():
    request = ""
    DB_HOST = 'localhost'
    DB_USER = 'shahid'
    DB_USER_PASSWORD = '12345'
    # DB_NAME = '/backup/dbnames.txt'
    DB_NAME = 'unltd'
    BACKUP_PATH=''
    def __init__(self,req):
        self.BACKUP_PATH = None
        self.request = req

    def Delete_Backup(self,request):

        try:
            backupid=request.POST.get('backupid')
            backup = Backup.objects.get(id=backupid)
            fs = FileSystemStorage(location=DB_ROOT)

            if fs.exists(backup.filename):
                fs.delete(backup.filename)
            backup.delete()
            if request.method == "POST":
                return 'success'
        except Exception as e:
            print(e)
            if request.method=="POST":
                return 'Backup Not Deleted'

    def Take_Backup(self):

        db = connection.settings_dict['NAME']
        DATETIME = time.strftime('%m%d%Y-%H%M%S')

        TODAYBACKUPPATH = './unltd/static/dbbackup/'
        DATETIME = time.strftime('%m%d%Y-%H%M%S')
        filename=DATETIME+db+".sql"
        print(TODAYBACKUPPATH)
        if not os.path.exists(TODAYBACKUPPATH):
            os.makedirs(TODAYBACKUPPATH)
        dumpcmd = "mysqldump -u " + self.DB_USER + " -p" + self.DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH+"/"  + DATETIME+db + ".sql"
        #dumpcmd="mysql dump -u {0} -p {1} {2} > {3}\{4}.sql".format(self.DB_USER,self.DB_USER_PASSWORD,db,TODAYBACKUPPATH,db)
        os.system(dumpcmd)

        filesize=os.stat(TODAYBACKUPPATH+"/"+filename).st_size
        filesize=str(filesize >> 10) +" Kb"
        backup=Backup(filename=filename,filesize=filesize,process='manual',created_date=datetime.datetime.now())
        backup.save()
        return 'success'

        print(db)

    def Show_Backup(self):
        data = []
        backups = Backup.objects.all()
        for backup in backups:
            data.append(
                [backup.id, backup.filename, backup.filesize,backup.process, backup.created_date])
        context = {
            "Title": "Database Backup",
            "Head": ["#", "Backup File Name", "Backup File Size","Process", "Backup Date"],
            "Data": data,
        }
        return context