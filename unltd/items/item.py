import random
import string

from ..models import SMSPackages, ItemVariation, Itemofferoption
from ..models import Category,Subcategory,User,Itemdisplay,Item
from django.core.files.storage import FileSystemStorage
from datetime import datetime


class AddItems():
    request=''
    def __init__(self,req):
        self.request=req

    def Add_ItemImage(self):

            user = User.objects.filter(id=self.request.session['id'])[0]
            itemname = self.request.POST.get("itemname")
            displaytype = self.request.POST.get("dislpaytype")
            preparetime = self.request.POST.get('time')
            SubCategoryName = self.request.POST.get('subcategoryname')
            visible = self.request.POST.get('visible')
            detail = self.request.POST.get('Detail')
            varitationtitle = self.request.POST.getlist('varitationtitle[]')
            varitationdiscription = self.request.POST.getlist('varitationdiscription[]')
            amount = self.request.POST.getlist('charges[]')
            varitationdiscount = self.request.POST.getlist('varitationdiscount[]')
            if self.request.POST.get('file') != '':
                file = self.request.FILES['file']
                fs = FileSystemStorage()
                filename=(self.id_generator()+"_" + file.name).replace(" ", "")
                fs.save(filename, file)
            else:
                filename = ''

            subcategoryid = Subcategory.objects.filter(id=SubCategoryName)[0]
            check = Itemdisplay.objects.filter(userid=user).filter(displaytype=displaytype)
            if (check):
                uid = Itemdisplay.objects.filter(userid=user).filter(displaytype=displaytype)[0]
               

            else:

                display = Itemdisplay(userid=user, displaytype=displaytype)
                display.save()
                uid = Itemdisplay.objects.latest('id')


            item = Item(subcategoryid=subcategoryid, itemname=itemname, description=detail, visible=visible,
                        itemdisplayid=uid, preparetime=preparetime, itemimage=filename)
            item.save()
            itemid = Item.objects.latest('id')
            for i in range(0,len(amount)):
                variation=ItemVariation(itemid=itemid,title=varitationtitle[i],description=varitationdiscription[i],discount=varitationdiscount[i],price=amount[i])
                variation.save()
            return 'TRUE'

    def Add_offers(self):
        try:
            customoffer = self.request.POST.get("Offer")
            StartDate = self.request.POST.get("StartDate")
            EndDate = self.request.POST.get('EndDate')
            Charges = self.request.POST.get('Charges')
            hiddenid = self.request.POST.get('hiddenid')
            hiddenid = Item.objects.filter(id=hiddenid)[0]
            StartDate= datetime.strptime(StartDate, '%d %B %Y - %H:%M')
            EndDate= datetime.strptime(EndDate, '%d %B %Y - %H:%M')
            offer = Itemofferoption(itemid=hiddenid, customoffer=customoffer, price=Charges,
                                    startdate=StartDate, enddate=EndDate)
            offer.save()
            msg = 'Package Added Successfully'
            return (msg)
        except Exception as e:
            return (str(e))

    def View_Offers(self):
            data = []

            if self.request.POST.get('select1') != None:
                id=self.request.POST.get('select1')
            else:
                id=self.request.POST.get('select')

            itemid = Item.objects.filter(id=id)[0]

            for offer in Itemofferoption.objects.filter(itemid=itemid):
                data.append([offer.id,offer.customoffer,offer.price,offer.startdate,offer.enddate,id])
            context = {
                "Data": data,
            }
            return context



    def Fetch_SubCategories(self):
        try:
            records=[]
            #only Fetch categories where user id=sessionid

            packages = Subcategory.objects.all().filter(categoryid__userid=self.request.session['id'])
            for package in packages:
                records.append([package.id,package.subcategoryname])

            return (records)
        except Exception as e:
            return (str(e))

    def id_generator(self):
        td = datetime.now()
        tda = str(td).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')
        rnm = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        return tda + rnm


    def View_Items(self):
        try:
            data = []
            for item in Item.objects.all():
                variations=[]
                for variation in ItemVariation.objects.filter(itemid=item.id):
                    variations.append([variation.id,variation.title,variation.description,variation.discount,variation.price])
                data.append([item.id,item.itemname,item.preparetime,item.visible,item.itemdisplayid.displaytype,item.subcategoryid.subcategoryname,item.itemimage,variations])
            context = {
             "Data": data,
            }
            return context
        except Exception as e:
            return e

class EditItems():
    request = ''
    idforedit = ''

    def __init__(self, req, cid):
        self.request = req
        self.idforedit = cid
    def Item_Delete(self):
            if(self.idforedit[0]=='a'):
                delete = ItemVariation.objects.filter(id=int(self.idforedit[1:])).delete()
            else:
                for variation in ItemVariation.objects.filter(itemid=int(self.idforedit)):
                    dele=ItemVariation.objects.filter(id=variation.id).delete()
                for file in Item.objects.filter(id=self.idforedit):
                    filename=file.itemimage
                print(filename)
                delete = Item.objects.filter(id=self.idforedit).delete()
                fs = FileSystemStorage()

                if fs.exists(filename):
                    fs.delete(filename)

            return ("Succesfully Deleted", self.idforedit)

    def Edit_Items(self):
        try:
            if (self.idforedit[0] == 'a'):
                self.idforedit = ItemVariation.objects.get(id=self.idforedit[1:]).itemid.id
            print(self.idforedit)
            data = []
            records=[]
            for item in Item.objects.filter(id=self.idforedit):
                variations = []
                for variation in ItemVariation.objects.filter(itemid=item.id):
                    variations.append(
                        [variation.id, variation.title, variation.description, variation.discount, variation.price])
                data.append([item.id, item.itemname, item.itemdisplayid.displaytype,item.preparetime,  item.subcategoryid.id,item.subcategoryid.subcategoryname,item.visible,
                             item.description,'ItemEditingFunction()', 'Edit Item', self.idforedit, item.itemimage, variations])
                packages = Subcategory.objects.all()
                for package in packages:
                    records.append([package.id, package.subcategoryname])

            context = {
                "Data": data,
                "Records":records,
                "Options": [['Yes', 1],['No',0]],
                "Settings": self.request.session['currency'],
            }
            return context
        except Exception as e:
            return "False"




    def Editing_Items(self):

            user = User.objects.filter(id=self.request.session['id'])[0]
            Hiddenid=self.request.POST.get('hiddenid')
            itemname = self.request.POST.get("itemname")
            displaytype = self.request.POST.get("dislpaytype")
            preparetime = self.request.POST.get('time')
            SubCategoryName = self.request.POST.get('subcategoryname')
            visible = self.request.POST.get('visible')
            detail = self.request.POST.get('Detail')
            varitationtitle = self.request.POST.getlist('varitationtitle[]')
            varitationdiscription = self.request.POST.getlist('varitationdiscription[]')
            amount = self.request.POST.getlist('charges[]')
            varitationdiscount = self.request.POST.getlist('varitationdiscount[]')
            print("itemdisplay",displaytype)
            obj=AddItems('')
            if self.request.POST.get('file') != '':
                file = self.request.FILES['file']
                fs = FileSystemStorage()
                filename=(obj.id_generator()+"_" + file.name).replace(" ", "")
                fs.save(filename, file)
            else:
                filename=Item.objects.get(id=Hiddenid).itemimage
            subcategoryid = Subcategory.objects.filter(id=SubCategoryName)[0]
            check = Itemdisplay.objects.filter(userid=user).filter(displaytype=displaytype)
            if (check):
                uuid = Itemdisplay.objects.filter(userid=user).filter(displaytype=displaytype)
                for i in uuid:
                    uid=i.id
            else:
                display = Itemdisplay(userid=user, displaytype=displaytype)
                display.save()
                uid = Itemdisplay.objects.latest('id')
            olditems=[]
            for variation in ItemVariation.objects.filter(itemid=Hiddenid):
                olditems.append(variation.id)
            itemid=Item.objects.filter(id=Hiddenid)[0]
            if(len(amount)>len(olditems)):
                #add new items
                for i in range(len(olditems),len(amount)):
                    variation = ItemVariation(itemid=itemid, title=varitationtitle[i], description=varitationdiscription[i],discount=varitationdiscount[i], price=amount[i])
                    variation.save()
            else:
                for i in range(0, len(amount)):

                        variationitem=ItemVariation.objects.filter(id=olditems[i]).update( title=varitationtitle[i], description=varitationdiscription[i],
                                              discount=varitationdiscount[i], price=amount[i])
                ab = Item.objects.filter(id=Hiddenid).update(subcategoryid=subcategoryid, itemname=itemname, description=detail, visible=visible,itemdisplayid=uid, preparetime=preparetime, creationdate=datetime.now(), itemimage=filename)
            return 'TRUE'


    def Offer_Delete(self):

            delete = Itemofferoption.objects.filter(id=self.idforedit).delete()
            return ("Succesfully Deleted", self.idforedit)


    def Edit_Offer(self):
        try:
            data = []
            for offer in Itemofferoption.objects.filter(id=self.idforedit):
                data.append([offer.id,offer.customoffer,offer.price,offer.startdate,offer.enddate,offer.itemid.id])
            context = {
                "Data": data,
                "Button":["Edit Offers","EditOffer()"],
                "Settings": self.request.session['currency'],
                "Id":data[0][0],
            }
            print(context)
            return context
        except Exception as e:
            return "False"

    def Editing_Offers(self):
            customoffer = self.request.POST.get("offername")
            StartDate = self.request.POST.get("startdate")
            EndDate = self.request.POST.get('expirydate')
            Charges = self.request.POST.get('charges')
            hiddenid = self.request.POST.get('hiddenid')
            # StartDate = datetime.strptime(StartDate, '%b %d %Y %I:%M%p')
            # EndDate = datetime.strptime(EndDate, '%b %d %Y %I:%M%p')
            StartDate = datetime.strptime(StartDate, '%d %B %Y - %H:%M')
            EndDate = datetime.strptime(EndDate, '%d %B %Y - %H:%M')
            user = User.objects.filter(id=self.request.session['id'])[0]
            ab = Itemofferoption.objects.filter(id=hiddenid).update(customoffer=customoffer, price=Charges, startdate=StartDate, enddate=EndDate)
            return 'TRUE'
