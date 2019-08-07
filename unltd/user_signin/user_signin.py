from ..models import User
class UserAuthenticate():
    request = ""

    def __init__(self, req):
        self.request = req
    def UserAuth(self):
        data = []
        dic = {}
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = User.objects.get(email=username , password=password )
        # for user in users:
        dic = {
                'Id':user.id,
               'UserId':user.userid,
               'DisplayName':user.displayname,
               'Email':user.email,
               'Mobile':user.mobile,
               'Password':user.password,
               'Image':user.image,
               'RegisterDate':user.registerdate,
               'LastUpdatedDate':user.lastupdateddate,
               'Status':user.status,
               'ForgotPassword':user.forgotpassword,
               'UserType':user.usertype
              }
        data.append(dic)
        context = {
             "Data": data
        }
        return context