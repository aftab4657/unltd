from ..models import SMSPackages,User,GeneralSetting
class ViewSMSPackages():
    request = ""

    def __init__(self, req):
        self.request = req
    def View_SMSPackages(self):
        data = []

        packages=SMSPackages.objects.all()
        for package in packages:
            data.append([package.smspackagetype,package.smspackagecharges,package.smspackagename,package.smspackageduration,package.id,package.totalsms])
        context = {
             "Data": data,
            "Settings": self.request.session['currency'],
        }
        return context