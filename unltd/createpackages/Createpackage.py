from unittest.test.testmock.testpatch import Foo
from django.utils import timezone
from unltd.models import Packages, Location,GeneralSetting,User
import smtplib
from random import randint
from datetime import datetime

class CreatePackage():
    request=''
    def __init__(self,req):
        self.request=req
    def Create_packages(self):
        try:
            PackageName = self.request.POST.get("PackageName")
            PackageDetail = self.request.POST.get("PackageDetail")
            PackageDuration = self.request.POST.get('PackageDuration')
            charges = self.request.POST.get('charges')
            Pakagetype = self.request.POST.get('PackageType')
            pack=Packages( packagename=PackageName,packagetype=Pakagetype, packagedetail=PackageDetail, packageduration=PackageDuration,packagecharges=charges,packagecreationdate=datetime.now())
            pack.save()
            msg = 'Package Added Successfully'
            return (msg)
        except Exception as e:
            return (str(e))

class EditPackages():
    request = ''
    idforedit=''
    def __init__(self, req,pid):
        self.request = req
        self.idforedit=pid
    def Packgae_Edit(self):
        data = []
        result=Packages.objects.filter(id=self.idforedit)
        for package in result:
            duration = (package.packageduration)
            data.append([package.packagename,package.packagetype,package.packageduration,package.packagecharges,package.packagedetail,'package_Editing()','Edit Package',self.idforedit])
        if(len(data)>=1):
            context = {
                 "Data": data,
                "Settings": self.request.session['currency'],
                "Options": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            }

        return context

    def Editing_Package(self):
        try:
            PackageName = self.request.POST.get("PackageName")
            PackageDetail = self.request.POST.get("PackageDetail")
            PackageDuration = self.request.POST.get('PackageDuration')
            charges = self.request.POST.get('charges')
            Pakagetype = self.request.POST.get('PackageType')
            Hiddenid=self.request.POST.get('hiddenid')
            updatepackage=Packages.objects.filter(id=Hiddenid).update( packagename=PackageName,packagetype=Pakagetype, packagedetail=PackageDetail, packageduration=PackageDuration,packagecharges=charges,packagecreationdate=datetime.now())
            msg = 'Package Added Successfully'
            print(Hiddenid)
            return (msg)

        except Exception as e:
            return (str(e))

    def Delete(self):
        try:
            deletepackage = Packages.objects.filter(id=self.idforedit).delete()
            return ("Succesfully Deleted",self.idforedit)

        except Exception as e:
            return (str(e))

