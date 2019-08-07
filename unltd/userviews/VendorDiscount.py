import datetime

from unltd.models import User, VendorDiscount


class Discount():
    request = ""

    def __init__(self,req):
        self.request = req

    def Create_Discount(self,check):
        if self.request.method == "POST":
            title = self.request.POST.get('Title',"")
            type = self.request.POST.get('Type',"")
            discount = self.request.POST.get('Discount',"")
            expirydate = self.request.POST.get('ExpiryDate',"")
            try:
                expirydate = datetime.datetime.strptime(expirydate, '%d %B %Y - %H:%M')
            except:
                try:
                    expirydate = expirydate.replace("a.m.","AM").replace("p.m.","PM")
                    expirydate = datetime.datetime.strptime(expirydate, '%b. %d, %Y, %I:%M %p')
                except:
                    expirydate = expirydate.replace("midnight","00:00")
                    expirydate = datetime.datetime.strptime(expirydate, '%b. %d, %Y, %H:%M')
            if(check == 'create'):
                user = User.objects.get(id=4)
                VendorDiscount(title=title,discount=discount,expirydate=expirydate,userid=user,type=type).save()
            elif(check == 'update'):
                id = self.request.POST.get('Id',"")
                VendorDiscount.objects.filter(id=id).update(title=title,discount=discount,expirydate=expirydate,type=type)
            return { "Head": ["Id","Title","DiscountType","Discount","CreatedDate","ExpiryDate"],
                     "Data": self.Get_Discounts()}

    def Get_Discounts(self):
        data = []
        discounts = VendorDiscount.objects.filter(userid=4)
        for discount in discounts:
            data.append([discount.id,discount.title,discount.type,discount.discount,discount.createdat,discount.expirydate])
        return data

    def Get_DiscountData(self):
        if self.request.method == "POST":
            id = self.request.POST.get('select',"")
            discount = VendorDiscount.objects.get(id=id)
            return {"Head":"Update/Delete",
                    "Data":[discount.title,discount.discount,discount.expirydate,discount.id,discount.type]}

    def Delete_Discount(self):
        if self.request.method == "POST":
            id = self.request.POST.get('Remove', "")
            VendorDiscount.objects.filter(id=id).delete()
            return { "Head": ["Id","Title","DiscountType","Discount","CreatedDate","ExpiryDate"],
                     "Data": self.Get_Discounts()}



