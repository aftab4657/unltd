from ..models import Superadmin
class SuperAdmin():
    request = ""

    def __init__(self, req):
        self.request = req
    def SuperAdminAuthenticate(self):
        data = []
        users=Superadmin.objects.all()
        for user in users:
            data.append([user.username,user.password])
        context = {
             "Data": data
        }
        return context