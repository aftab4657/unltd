from unittest.test.testmock.testpatch import Foo
from django.utils import timezone
import smtplib
from random import randint
from datetime import datetime

from ..models import SMSPackages,GeneralSetting,User


class CreateSMSPackage():
    request=''
    def __init__(self,req):
        self.request=req
    def Create_SMSpackages(self):
        try:
            PackageName = self.request.POST.get("PackageName")
            PackageDetail = self.request.POST.get("PackageDetail")
            PackageDuration = self.request.POST.get('PackageDuration')
            charges = self.request.POST.get('charges')
            total = self.request.POST.get('total')
            Pakagetype = self.request.POST.get('PackageType')
            pack=SMSPackages( smspackagename=PackageName,smspackagetype=Pakagetype, smspackagedetail=PackageDetail, smspackageduration=PackageDuration,smspackagecharges=charges,packagecreationdate=datetime.now(),totalsms=total)
            pack.save()
            msg = 'SMS Package Added Successfully'
            return (msg)
        except Exception as e:
            return (str(e))

class EditSMSPackages():
    request = ''
    idforedit=''
    def __init__(self, req,pid):
        self.request = req
        self.idforedit=pid
    def Packgae_SMSEdit(self):
        data = []
        result=SMSPackages.objects.filter(id=self.idforedit)
        for package in result:
            data.append([package.smspackagename,package.smspackagetype,package.smspackageduration,package.smspackagecharges,package.smspackagedetail,'package_SMSEditing()','Edit SMS Package',self.idforedit,package.totalsms])
        if(len(data)>=1):
            context = {
                 "Data": data,
                "Settings": self.request.session['currency'],
                "Options": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

            }


        return context

    def Editing_PackageSMS(self):

            PackageName = self.request.POST.get("PackageName")
            PackageDetail = self.request.POST.get("PackageDetail")
            PackageDuration = self.request.POST.get('PackageDuration')
            currency = str(self.request.POST.get('currency'))
            charges = self.request.POST.get('charges')
            Pakagetype = self.request.POST.get('PackageType')
            total = self.request.POST.get('total')
            Hiddenid=self.request.POST.get('hiddenid')
            updatesmspackage=SMSPackages.objects.filter(id=Hiddenid).update( smspackagename=PackageName,smspackagetype=Pakagetype,smspackagecharges=charges, smspackagedetail=PackageDetail, smspackageduration=PackageDuration,packagecreationdate=datetime.now(),totalsms=total)
            msg = 'SMS Package Added Successfully'
            return (msg)




    def SMSDelete(self):
        try:
            deletepackage = SMSPackages.objects.filter(id=self.idforedit).delete()
            return ("Succesfully Deleted",self.idforedit)

        except Exception as e:
            return (str(e))

