
from ..models import Category,Subcategory,User
from datetime import datetime



class CreateCategories():
    request=''
    def __init__(self,req):
        self.request=req
    def Create_Categories(self):
        try:
            user = User.objects.filter(id=self.request.session['id'])[0]
            CategoryName = self.request.POST.get("CategoryName")
            CategoryDuration = self.request.POST.get('CategoryDuration')
            CategoryDuration= datetime.strptime(CategoryDuration, '%d %B %Y - %H:%M')
            pack = Category(userid=user, categoryname=CategoryName, timerange=CategoryDuration)
            pack.save()
            msg = 'SMS Package Added Successfully'
            return (msg)
        except Exception as e:
            return (str(e))
    def Create_SubCategories(self):
        try:
            SubCategoryName = self.request.POST.get("SubCategoryName")
            CategoryName = self.request.POST.get("CategoryName")
            SubCategoryDuration = self.request.POST.get('SubCategoryDuration')
            category = Category.objects.filter(id=CategoryName)[0]
            SubCategoryDuration= datetime.strptime(SubCategoryDuration, '%d %B %Y - %H:%M')

            p=Subcategory(subcategoryname=SubCategoryName, timerange=SubCategoryDuration,categoryid=category)
            p.save()
            msg = 'SMS Package Added Successfully'
            return (msg)
        except Exception as e:
            return (str(e))

    def Fetch_Categories(self):
        try:
            records=[]
            packages = Category.objects.all().filter(userid=self.request.session['id'])
            for package in packages:
                records.append([package.id,package.categoryname])

            return (records)
        except Exception as e:
            return (str(e))
    def View_Categories(self):
        data = []
        packages=Category.objects.all().filter(userid=self.request.session['id'])
        for package in packages:
            data.append([package.id, package.categoryname,package.timerange])
        context = {
         "Data": data,
    }
        return context

    def View_SubCategories(self):
        data = []
        packages=Subcategory.objects.all().filter(categoryid__userid=self.request.session['id'])
        for package in packages:
            data.append([package.id, package.subcategoryname,package.timerange,package.categoryid.categoryname])
        context = {
         "Data": data,

        }

        return context

class EditCategories():
    request = ''
    idforedit=''
    def __init__(self, req,cid):
        self.request = req
        self.idforedit=cid
    def Edit_Categories(self):
        data = []
        result=Category.objects.filter(id=self.idforedit)
        for package in result:
            data.append([ package.categoryname, package.timerange,'CategoryEditingFunction()','Edit Category',self.idforedit])


        return data

    def Editing_Categoryy(self):
            CategoryName = self.request.POST.get("CategoryName")
            CategoryDuration = self.request.POST.get("CategoryDuration")
            Hiddenid=self.request.POST.get('hiddenid')
            updatecategory=Category.objects.filter(id=Hiddenid).update( categoryname=CategoryName,timerange=CategoryDuration,creationdate=datetime.now())
            msg = 'Category Added Successfully'
            return (msg)

    def Category_Delete(self):
        try:
            deletepackage = Category.objects.filter(id=self.idforedit).delete()
            return ("Succesfully Deleted",self.idforedit)

        except Exception as e:
            return (str(e))

    def Edit_SubCategories(self):
        data = []
        records=[]
        result = Subcategory.objects.filter(id=self.idforedit)
        for package in result:
            data.append(
                [package.subcategoryname, package.timerange,package.categoryid.categoryname, 'SubCategoryEditingFunction()', 'Edit Sub-Category', self.idforedit,package.categoryid.id])
        packagess = Category.objects.all()
        for package in packagess:
            records.append([package.id, package.categoryname])

        context = {
            "Data": data,
            "Records":records,
            "Options": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        }
        return context
    def Editing_SubCategoryy(self):
            SubCategoryName = self.request.POST.get("SubCategoryName")
            CategoryName = self.request.POST.get("CategoryName")
            SubCategoryDuration = self.request.POST.get('SubCategoryDuration')
            Hiddenid=self.request.POST.get('hiddenid')

            category = Category.objects.filter(id=CategoryName)[0]
            updatecategory=Subcategory.objects.filter(id=Hiddenid).update( subcategoryname=SubCategoryName,timerange=SubCategoryDuration, categoryid=category,creationdate=datetime.now())
            msg = 'Category Added Successfully'
            return (msg)

    def SubCategory_Delete(self):
        try:
            deletepackage = Subcategory.objects.filter(id=self.idforedit).delete()
            return ("Succesfully Deleted",self.idforedit)

        except Exception as e:
            return (str(e))
