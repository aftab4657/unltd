from unltd.models import Vendor,User
from django.core.files.storage import FileSystemStorage
import random,string,datetime
class Profiles():
    request = ''
    def id_generator(self):
        td = datetime.datetime.now()
        tda = str(td).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')
       # rnm = ''.join(random.choice(string.ascii_uppercase+ string.digits) for _ in range(9))
        return tda#+rnm
    def __init__(self,req):
        self.request = req
    def Vendor_Signup(self):
        try:
            bname = self.request.POST.get('bname')
            bemail = self.request.POST.get('bemail')
            baddress = self.request.POST.get('baddress')
            bphone = self.request.POST.get('bphone')
            industry = self.request.POST.get('industry')
            sname = self.request.POST.get('sname')
            blogo = self.request.FILES['blogo']
            fs = FileSystemStorage()
            blogon = self.id_generator()+"_"+blogo.name
            fs.save(blogon, blogo)
            bicon = self.request.FILES['bicon']
            fs = FileSystemStorage()
            biconn = self.id_generator()+"_"+bicon.name
            fs.save(biconn, bicon)
            hicon = self.request.FILES['hicon']
            fs = FileSystemStorage()
            hiconn = self.id_generator()+"_"+hicon.name
            fs.save(hiconn, hicon)
            try:
                vid = User.objects.filter(id=1)[0]
                Vendor.objects.filter(userid=1).delete()
                b = Vendor(userid=vid, businessname=bname, businessemail=bemail, businesscontact=bphone, industry=industry, systemname=sname,businessaddress=baddress,businesslogo=blogon,businessicon=biconn,heroicon=hiconn)
                b.save()
                return 'Saved'
            except Exception as x:
                return 'X='+str(x)
           # return vcode
        except Exception as t3:
            return 'T3='+str(t3)
