from ..models import User

class Validation():
    request = ''
    def __init__(self,req):
        self.request = req
    def Email_Check(self):
        obj = User.objects.all()
        mail = self.request.POST.get('email')
        for x in obj:
            if(x.email==mail):
                return 'taken'
    def password_Check(self):
        userid = self.request.session.get('id', "")
        fpassword = self.request.POST.get('password')
        sample_instance = User.objects.get(id=userid)
        xpass = sample_instance.password
        if(fpassword!=xpass):
          return 'notmatch'
