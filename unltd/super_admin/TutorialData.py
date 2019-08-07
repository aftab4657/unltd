import datetime
import string
import random
from string import ascii_uppercase, digits

from ..models import Vendor, Staff, Member, Tutorial, Superadmin, User, TutorialType
from django.core.files.storage import FileSystemStorage


class TutorialView():
    request = ""
    def __init__(self,req):
        self.request = req

    def id_generator(self):
        td = datetime.datetime.now()
        tda = str(td).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')
        rnm = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        return tda + rnm

    def Show_Vendor_Tutorial(self):
        data = []
        tutorials = Tutorial.objects.filter(group='vendor')
        for tutorial in tutorials:
            data.append(
                [tutorial.id, tutorial.feature_image,tutorial.title,tutorial.type.name, tutorial.created_date])
        context = {
            "Title": "Tutorials",
            "Head": ["#", "Image","Title","Category","Created Date"],
            "Data": data,
        }
        return context
    def Show_Customer_Tutorial(self):
        data = []
        tutorials = Tutorial.objects.filter(group='customer')
        for tutorial in tutorials:
            data.append(
                [tutorial.id, tutorial.feature_image,tutorial.title,tutorial.type.name, tutorial.created_date])
        context = {
            "Title": "Tutorials",
            "Head": ["#", "Image","Title","Category","Created Date"],
            "Data": data,
        }
        return context

    def Show_Tutorial_Type(self):
        data = []
        tutorialstype = TutorialType.objects.all().order_by('id')
        for type in tutorialstype:
            data.append(
                [type.id, type.name])
        context = {
            "Title": "Tutorial Types",
            "Head": ["#", "Name"],
            "Data": data,
        }
        return context

    def Show_Tutorial_Detail(self,request):
        data=[]
        tutorial_id = request.GET.get('id')
        print(tutorial_id)
        tutorial=Tutorial.objects.get(id=tutorial_id)
        data=[tutorial.id,tutorial.title,tutorial.type, tutorial.feature_image, tutorial.long_text]
        for items in data:
            print(items)
        context = {
            "Title": "Tutorial Details",
            "Data": data,
        }
        return context

    def Edit_Tutorial(self,request):
        data=[]
        if 'tutorialid' not in request.POST:
            tutorial_id = None
        else:
            tutorial_id = request.POST['tutorialid']
        if tutorial_id is not None:
            tutorial=Tutorial.objects.get(id=tutorial_id)
            print(tutorial_id)
            # imagepath=request.get_path()+"/static/media"+tutorial.feature_image
            data=[tutorial.id,tutorial.title,tutorial.type, tutorial.feature_image, tutorial.long_text]
            context=self.Show_Tutorial_Type()
            print(context['Data'])
        for items in data:
            print(items)
        context = {
            "Title": "Edit Tutorial",
            "Data": data,
            "TutorialType":context['Data']
        }
        return context

    def Add_Tutorial(self,request):
        data = []
        try:
            filename=self.id_generator()

            file = request.FILES['tutorialimage']
            filenames = str(file.name)
            filextension=filenames.split('.')
            filename=filename+"."+filextension[-1]
            fs = FileSystemStorage()

            if fs.exists(filename):
                fs.delete(filename)
                fs.save(filename, file)
            else:
                fs.save(filename, file)
            long_text=request.POST.get('description')
            title=request.POST.get('title')
            created_date=datetime.datetime.now()
            group=request.POST.get('tutorialgroup')
            #created_by=User.objects.get(id=request.session['id'])
            created_by=User.objects.get(id=1)
            type=TutorialType.objects.get(id=request.POST.get('tutorialtype'))

            tutorial = Tutorial(title=title,long_text=long_text,
                                created_by=created_by,modified_date=created_date,
                                created_date=created_date,feature_image=filename,type=type,group=group)
            tutorial.save()
            obj = Tutorial.objects.latest('id')
            if request.method == "POST":
                return 'success'
        except Exception as e:
            print("XXXXXXXXXXXXXXXX")
            #print(request.session['id'])
            print(e)
            if request.method=="POST":
                return 'Tutorial Not Added'

    def Add_Tutorial_Type(self,request):
        data = []
        try:
            name=request.POST.get('tutorial_name')
            #created_by=User.objects.get(id=request.session['id'])

            tutorialtype = TutorialType(name=name)
            tutorialtype.save()
            if request.method == "POST":
                return 'success'
        except Exception as e:
            print(e)
            if request.method=="POST":
                return e
    
    def Delete_Tutorial_Type(self,request):
        try:
            if request.method == "POST":
                tutorialtypeid=request.POST.get('tutorialtypeid')
                tutorial=Tutorial.objects.get(type=tutorialtypeid)
                tutorial.delete()
                tutorialtype = TutorialType.objects.get(id=tutorialtypeid)
                tutorialtype.delete()
                return 'success'
        except Exception as e:
            print(e)
            if request.method=="POST":
                return 'Tutorial Not Added'

    def Edit_Tutorial_Type(self,request):
        data=[]
        if 'tutorialtypeid' not in request.POST:
            tutorialtypeid = None
        else:
            tutorialtypeid = request.POST['tutorialtypeid']
        if tutorialtypeid is not None:
            type=TutorialType.objects.get(id=tutorialtypeid)
            print(type)
            data=[type.id,type.name,]
        for items in data:
            print(items)
        context = {
            "Data": data,
        }
        return context

    def Update_Tutorial(self,request):
        data = []
        try:

            print('image selected')
            file = request.FILES.get('tutorialimage',False)
            if file:
                filename=self.id_generator()
                fs = FileSystemStorage()
                filenames = str(file.name)
                filextension = filenames.split('.')
                filename = filename + "." + filextension[-1]


                if fs.exists(filename):
                    fs.delete(filename)
                    fs.save(filename, file)
                else:
                    fs.save(filename, file)
            long_text=request.POST.get('description')
            title=request.POST.get('title')
            #created_date=datetime.datetime.now()
            #created_by=User.objects.get(id=request.session['id'])
            tutorialid=request.POST.get('tutorialid')
            tutorialtype=TutorialType.objects.get(id=request.POST.get('tutorialtype'))
            tutorial=Tutorial.objects.get(id=tutorialid)
            tutorial.title=title
            tutorial.type=tutorialtype
            tutorial.long_text=long_text
            if file:
                print('image selected')
                tutorial.feature_image=file.name
            tutorial.modified_date=datetime.datetime.now()
            tutorial.save()
            #obj = Tutorial.objects.latest('id')
            if request.method == "POST":
                return 'success'
        except Exception as e:
            print(e)
            if request.method=="POST":
                return 'Tutorial Not Added'

    def Delete_Tutorial(self,request):
        try:
            tutorialid=request.POST.get('tutorialid')
            tutorial = Tutorial.objects.get(id=tutorialid)
            imagename=tutorial.feature_image
            fs = FileSystemStorage()

            if fs.exists(imagename):
                fs.delete(imagename)
            tutorial.delete()
            if request.method == "POST":
                return 'success'
        except Exception as e:
            print(e)
            if request.method=="POST":
                return 'Tutorial Not Added'

    def Update_Tutorial_Type(self, request):
        tutorialid=request.POST.get('tutorial_edit_id')
        tutorialtype=TutorialType.objects.get(id=tutorialid)
        tutorialtype.name=request.POST.get('tutorial_edit_name')
        tutorialtype.save()
        return 'success'
