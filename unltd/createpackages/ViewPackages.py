from ..models import Packages,GeneralSetting,User
class ViewPackages():
    request = ""

    def __init__(self, req):
        self.request = req
    def View_Packages(self):
        data = []
        packages=Packages.objects.all()
        for package in packages:
            data.append([package.packagetype,package.packagecharges,package.packagename,package.packageduration,package.id])
        context = {
             "Data": data,
            "Settings":self.request.session['currency']
        }
        return context
class FetchGenralSettings():
    request = ""

    def __init__(self, req):
        self.request = req
    def Fetch_Settings(self):
        settings = []
        id = self.request.session['id']
        user = User.objects.filter(id=id)[0]
        packages=GeneralSetting.objects.filter(userid=id)
        for package in packages:
            settings.append([package.language,package.currency])
        return settings