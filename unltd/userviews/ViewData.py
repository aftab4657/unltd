from UNLTDjango.settings import BASE_DIR
from ..models import Vendor,Staff,Member,Messages,Messagesender,User,Location,Itemorder,RechargeHistory,Tables,Booking,Subcategory,Item,ItemVariation,Orders,Venderorders,VendorStaff,VendorMember, VendorDiscount
import smtplib,requests,urllib.parse,os,qrcode,datetime
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.utils import timezone
class UserViews():
    request = ""
    def __init__(self,req):
        self.request = req

    def Vendor_View(self):
        data = []
        vendors = Vendor.objects.all().order_by('-userid__lastupdateddate')
        for vendor in vendors:
            data.append([vendor.userid.userid,vendor.userid.displayname,vendor.userid.email,vendor.userid.mobile,vendor.userid.registerdate,vendor.userid.status,vendor.businessname,vendor.businessemail,vendor.businesscontact,vendor.industry,vendor.systemname])
        context = {
            "Title": "Vendors",
            "Head": ["Id", "Name","Email","Mobile","Register Date","Status","Business Name","Business Email","Business Contact","Industry","System Name"],
            "Data": data,
        }
        return context

    def Staff_View(self):
        staffs = Staff.objects.all().order_by('-userid__lastupdateddate')
        return self.Get_Staff(staffs)

    def Vendor_Staff_View(self):
        staffs = Staff.objects.filter(vendor__userid=4).order_by('-userid__lastupdateddate')
        return self.Get_Staff(staffs)

    def Get_Staff(self,staffs):
        data = []
        for staff in staffs:
            data.append(
                [staff.userid.userid,staff.userid.displayname, staff.userid.email, staff.userid.mobile, staff.userid.registerdate,
                 staff.userid.status, staff.privilege,staff.department])
        context = {
            "Title": "Staff",
            "Head": ["Id", "Name", "Email", "Mobile", "Register Date", "Status", "Previllages", "Department"],
            "Data": data,
        }
        return context

    def Member_View(self):
        members = Member.objects.all().order_by('-userid__lastupdateddate')
        return self.Get_Member(members)

    def Vendor_MemberView(self):
        members = Member.objects.filter(vendor__userid=4).order_by('-userid__lastupdateddate')
        return self.Get_Member(members)

    def Get_Member(self,members):
        data = []
        for member in members:
            data.append(
                [member.userid.userid,member.userid.displayname, member.userid.email, member.userid.mobile, member.userid.registerdate,
                 member.userid.status, member.dateofbirth,member.gender])
        context = {
            "Title": "Members",
            "Head": ["Id", "Name", "Email", "Mobile", "Register Date", "Status", "Date Of Birth","Gender"],
            "Data": data,
        }
        return context

    def Return_Record(self):
        userid = self.request.POST.get('select',"")
        type = self.request.POST.get('type',"")
        if type == "Vendors":
            users = Vendor.objects.filter(userid__userid = userid)
            for user in users:
                return user.userid.email,user.userid.mobile
        elif type == "Staff":
            users = Staff.objects.filter(userid__userid=userid)
            for user in users:
                return user.userid.email, user.userid.mobile
        elif type == "Members":
            users = Member.objects.filter(userid__userid=userid)
            for user in users:
                return user.userid.email, user.userid.mobile

class MailSend():
    emailid =''
    subject = ''
    body = ''
    userid = ''
    contact = ''
    type = ''
    def __init__(self,emailid,subject,body,userid,contact):
        self.emailid = emailid
        self.subject = subject
        self.body = body
        self.userid = userid
        self.contact = contact

    def Send_Email(self):
        self.type = 'email'
        gmail_user = 'softwarepatterns005@gmail.com'
        gmail_password = 's00998877'
        sent_from = gmail_user
        to = [self.emailid]
        subject = self.subject
        body = self.body
        email_text = """\  
        From: %s  
        To: %s  
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            self.SaveMessageToDb()

            return ('Email Send Successfully')
        except Exception as error:
           return (str(error))

    def SaveMessageToDb(self):
        sender = User.objects.filter(pk=1)[0]
        vendorid = Messagesender(userid=sender)
        vendorid.save()
        reciever = User.objects.filter(userid=self.userid)[0]
        Messages(senderid = vendorid, receiverid = reciever, type = self.type, messagehead = self.subject, messagebody = self.body).save()

    def Send_SMS(self):
        try:
            self.type = 'sms'
            mobile = self.contact
            #mobile = "" # Recepient Mobile  Number
            sender = "SenderID"
            message = self.body

            url = "http://sendpk.com/api/sms.php?username=923369298309&password=5314";
            post = "sender="+urllib.parse.quote(sender)+"&mobile="+urllib.parse.quote(mobile)+"&message="+urllib.parse.quote(message)

            requests.post(url, params=post)

            self.SaveMessageToDb()
            return "SMS Send Successfully"
        except Exception as error:
            return str(error)

class GetData():
    request = ''
    def __init__(self,request):
        self.request = request

    def Get_Data_And_Template(self):
        from django.db import connection
        cursor = connection.cursor()
        type = self.request.POST.get('type',"")
        userid = self.request.POST.get('select',"")
        if type == "Vendors":
            vendor = []
            cursor.execute("SELECT user.DisplayName, user.Email, location.Country, location.State, location.city, location.PostCode, location.Address, user.Mobile, vendor.BusinessName, vendor.BusinessEmail, vendor.BusinessContact, vendor.Industry,vendor.SystemName, vendor.BusinessAddress, user.Id FROM user LEFT JOIN vendor ON user.Id = vendor.UserId LEFT JOIN location ON user.Id = location.UserId WHERE user.UserId = '" + userid + "'")
            for row in cursor.fetchall():
                vendor = row
            return "vendormanagement/updatevendor.html",vendor
        elif type == "Staff":
            staff = []
            cursor.execute("SELECT user.DisplayName, user.Email, location.Country, location.State, location.city, location.PostCode, location.Address, user.Mobile, staff.Privilege, staff.Department, user.Id FROM user LEFT JOIN staff ON user.Id = staff.UserId LEFT JOIN location ON user.Id = location.UserId WHERE user.UserId = '" + userid + "'")
            for row in cursor.fetchall():
                staff = row
            return "vendormanagement/updatestaff.html",staff
        elif type == "Members":
            member = []
            cursor.execute("SELECT user.DisplayName, user.Email, location.Country, location.State, location.city, location.PostCode, location.Address, user.Mobile, member.Gender, member.DateOfBirth, user.Id FROM user LEFT JOIN member ON user.Id = member.UserId LEFT JOIN location ON user.Id = location.UserId WHERE user.UserId = '" + userid + "'")
            for row in cursor.fetchall():
                member = row
            return "vendormanagement/updatemember.html",member

    def Vendor_Get_Data_And_Template(self):
        from django.db import connection
        cursor = connection.cursor()
        type = self.request.POST.get('type', "")
        userid = self.request.POST.get('select', "")
        if type == "Staff":
            staff = []
            cursor.execute(
                "SELECT user.DisplayName, user.Email, location.Country, location.State, location.city, location.PostCode, location.Address, user.Mobile, staff.Privilege, staff.Department, user.Id FROM user LEFT JOIN staff ON user.Id = staff.UserId LEFT JOIN location ON user.Id = location.UserId WHERE user.UserId = '" + userid + "'")
            for row in cursor.fetchall():
                staff = row
            return "VendorSystem/Vendor_UpdateStaff.html", staff
        elif type == "Members":
            member = []
            cursor.execute(
                "SELECT user.DisplayName, user.Email, location.Country, location.State, location.city, location.PostCode, location.Address, user.Mobile, member.Gender, member.DateOfBirth, user.Id FROM user LEFT JOIN member ON user.Id = member.UserId LEFT JOIN location ON user.Id = location.UserId WHERE user.UserId = '" + userid + "'")
            for row in cursor.fetchall():
                member = row
            return "VendorSystem/Vendor_UpdateMember.html", member
    def Get_PData_And_Template(self):
        from django.db import connection
        cursor = connection.cursor()
        userid = self.request.session.get('id', "")
        print (userid)
        profile = []
        cursor.execute(
            "SELECT user.DisplayName, user.Email, user.Mobile,user.image FROM user WHERE user.Id = '" + str(userid) + "'")
        for row in cursor.fetchall():
            profile = row
        return "ProfilesManagement/PersonalProfile.html", profile

    def id_generator(self):
        td = datetime.now()
        tda = str(td).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')
        # rnm = ''.join(random.choice(string.ascii_uppercase+ string.digits) for _ in range(9))
        return tda  # +rnm

    def Get_PUData_And_Template(self):
        from django.db import connection
        userid = self.request.session.get('id', "")
        dname = self.request.POST.get('dname')
        email = self.request.POST.get('email')
        phone = self.request.POST.get('phone')
        pavatar = ''
        pavatar = self.request.FILES['pavatar']
        fs = FileSystemStorage()
        pavatarn = self.id_generator() + "_" + pavatar.name
        fs.save(pavatarn, pavatar)
        User.objects.filter(id=userid).update(displayname=dname, email=email, mobile=phone, image=pavatarn,
                                              lastupdateddate=datetime.now(tz=timezone.utc))
        # profile = []
        # cursor.execute(
        #     "SELECT user.DisplayName, user.Email, user.Mobile, user.Id FROM user WHERE user.Id = '" + userid + "'")
        # for row in cursor.fetchall():
        #     profile = row
        # print (profile)
        # return "ProfilesManagement/PersonalProfile.html", profile

    def Update_Profile_Password(self):
        userid = self.request.session.get('id', "")
        fpassword = self.request.POST.get('password')
        try:
            User.objects.filter(id=userid).update(password=fpassword)
            return 'Success'
        except:
            return 'Not Success'


class UpdateUsers():
    request = ""
    userid,username,email,country,state,city,postcode,address,phonenumber = "","","","","","","","",""
    def __init__(self,req):
        self.request = req
        if self.request.method == "POST":
            self.userid = self.request.POST.get('userid',"")
            self.username = self.request.POST.get('dname',"")
            self.email = self.request.POST.get('useremail',"")
            self.country = self.request.POST.get('country',"")
            self.country = (self.country.split(","))[0]
            self.state = self.request.POST.get('state',"")
            self.city = self.request.POST.get('city',"")
            self.postcode = self.request.POST.get('postalcode',"")
            self.address = self.request.POST.get('address',"")
            self.phonenumber = self.request.POST.get('phone',"")
            User.objects.filter(id=self.userid).update(displayname=self.username, email=self.email,
                                                       mobile=self.phonenumber,lastupdateddate=datetime.datetime.now())
            Location.objects.filter(userid=self.userid).update(address=self.address, city=self.city,
                                                               postcode=self.postcode, state=self.state,
                                                               country=self.country)

    def Update_Vendor(self):
        if self.request.method == "POST":
            bname = self.request.POST.get('bname',"")
            bemail = self.request.POST.get('bemail',"")
            bphone = self.request.POST.get('bphone',"")
            industry = self.request.POST.get('industry',"")
            sname = self.request.POST.get('sname',"")
            baddress = self.request.POST.get('baddress',"")
            Vendor.objects.filter(userid=self.userid).update(businessname=bname, businessemail=bemail,
                                                             businesscontact=bphone, industry=industry,
                                                             systemname=sname, businessaddress=baddress)

    def Update_Staff(self):
        if self.request.method == "POST":
            privilege = self.request.POST.get('privilege',"")
            department = self.request.POST.get('department',"")
            Staff.objects.filter(userid=self.userid).update(privilege=privilege,department=department)

    def Update_Member(self):
        if self.request.method == "POST":
            gender = self.request.POST.get('gender',"")
            dob = self.request.POST.get('dob',"")
            Member.objects.filter(userid=self.userid).update(dateofbirth=dob,gender=gender)

class UpdatePassword():
    request,userid,password = "","",""
    def __init__(self,req):
        self.request = req
        if self.request.method == "POST":
            self.userid = self.request.POST.get('userid',"")
            self.password = self.request.POST.get('password',"")

    def Update_Password(self):
        User.objects.filter(userid=self.userid).update(password=self.password)
        user = User.objects.filter(userid=self.userid)[0]
        if user.usertype == "Vendor":
            vendor = UserViews(self.request)
            context = vendor.Vendor_View()
        elif user.usertype == "Staff":
            vendor = UserViews(self.request)
            context = vendor.Staff_View()
        else:
            vendor = UserViews(self.request)
            context = vendor.Member_View()

        return context

    def Vendor_Update_Password(self):
        User.objects.filter(userid=self.userid).update(password=self.password)
        user = User.objects.filter(userid=self.userid)[0]
        if user.usertype == "Staff":
            vendor = UserViews(self.request)
            context = vendor.Vendor_Staff_View()
        else:
            vendor = UserViews(self.request)
            context = vendor.Vendor_MemberView()

        return context

class UpdateStatus():
    request, userid, status = "", "", ""

    def __init__(self, req):
        self.request = req
        if self.request.method == "POST":
            self.userid = self.request.POST.get('userid', "")
            self.status = self.request.POST.get('status', "")

    def Updates_Status(self):
        User.objects.filter(userid=self.userid).update(status=self.status)
        user = User.objects.filter(userid=self.userid)[0]
        if user.usertype == "Vendor":
            vendor = UserViews(self.request)
            context = vendor.Vendor_View()
        elif user.usertype == "Staff":
            vendor = UserViews(self.request)
            context = vendor.Staff_View()
        else:
            vendor = UserViews(self.request)
            context = vendor.Member_View()
        return context

    def Vendor_Updates_Status(self):
        User.objects.filter(userid=self.userid).update(status=self.status)
        user = User.objects.filter(userid=self.userid)[0]
        if user.usertype == "Staff":
            vendor = UserViews(self.request)
            context = vendor.Vendor_Staff_View()
        else:
            vendor = UserViews(self.request)
            context = vendor.Vendor_MemberView()
        return context

class Subscription():
    request = ""
    def __init__(self,req):
        self.request = req

    def Get_Subscription_Invoices(self):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(
            """SELECT user.UserId, user.DisplayName, packages.PackageName, packages.PackageType, packages.PackageDuration,packages.PackageCharges, subscription.SubscriptionDate, subscription.ExpiryDate, subscription.AutoRenew, subscription.FreeTrail, subscription.ExpiryAlert, subscription.AutoRenew FROM subscription LEFT JOIN user ON subscription.UserId = user.Id LEFT JOIN packages ON subscription.PackageId = packages.Id """)

        for row in cursor.fetchall():
            renew,trail,expiryaltert,renewconfirmation = "","","",""
            if row[8] == 0:
                renew = "No"
            else:
                renew = "Yes"

            if row[9] == 0:
                trail = "No"
            else:
                trail = "Yes"

            if row[10] == 0:
                expiryaltert = "No"
            else:
                expiryaltert = "Yes"

            if row[11] == 0:
                renewconfirmation = "No"
            else:
                renewconfirmation = "Yes"

            data.append([row[0],row[1],row[2],row[3],str(row[4])+' Months',row[5],row[6],row[7],renew,trail,expiryaltert,renewconfirmation])
        context = {
            "Title": "Subscription Packages Details",
            "Head": ["Id", "Name","Package Name","Package Type","Duration","Package Charges","SubscriptionDate","ExpiryDate","Auto Renew","Free Trail","Expiry Alert","Renew Confirmation"],
            "Data": data,
        }
        return context

    def Get_SMSSubscription_Invoices(self):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""SELECT user.UserId, user.DisplayName, smspackages.SMSPackageName, smspackages.SMSPackageType , smspackages.SMSPackageDuration,smspackages.PackageCharges,smspackages.TotalSMS, smssubscription.SubscriptionDate, smssubscription.ExpiryDate, smssubscription.AutoRenew, smssubscription.FreeTrail, smssubscription.ExpiryAlert, smssubscription.AutoRenew FROM smssubscription LEFT JOIN user ON smssubscription.UserId = user.Id LEFT JOIN smspackages ON smssubscription.PackageId = smspackages.Id """)
        for row in cursor.fetchall():
            renew,trail,expiryaltert,renewconfirmation = "","","",""
            if row[9] == 0:
                renew = "No"
            else:
                renew = "Yes"

            if row[10] == 0:
                trail = "No"
            else:
                trail = "Yes"

            if row[11] == 0:
                expiryaltert = "No"
            else:
                expiryaltert = "Yes"

            if row[12] == 0:
                renewconfirmation = "No"
            else:
                renewconfirmation = "Yes"

            data.append([row[0],row[1],row[2],row[3],str(row[4])+' Months',row[5],row[6],row[7],row[8],renew,trail,expiryaltert,renewconfirmation])
        context = {
            "Title": "SMS Packages Details",
            "Head": ["Id", "Name","Package Name","Package Type","Duration","Package Charges","Total SMS","SubscriptionDate","ExpiryDate","Auto Renew","Free Trail","Expiry Alert","Renew Confirmation"],
            "Data": data,
        }
        return context

class Transaction():
    request = ""
    def __init__(self,req):
        self.request = req

    def Get_Transaction_Info(self):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(
            """SELECT user.DisplayName, transaction.Amount, transaction.Mode, transaction.Date, orders.OrderType, transaction.Cashier, transaction.Discount, transaction.Waiter, transaction.Id FROM transaction 
                      LEFT JOIN orders ON transaction.OrderId = orders.Id
                      LEFT JOIN user ON transaction.Member = user.Id """)

        for row in cursor.fetchall():
            cashier = User.objects.filter(id=row[5])[0]
            waiter = User.objects.filter(id=row[7])[0]
            data.append([row[0], row[2], row[1], row[3], row[4], cashier.displayname, row[6],waiter.displayname,row[8]])
        context = {
            "Head": ["Customer Name", "Mode","Amount","Date","Order Type","Cashier Name","Discount","Waiter Name"],
            "Data": data,
        }
        return context

    def Vendor_Get_Transaction_Info(self):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(
            """SELECT user.DisplayName, transaction.Amount, transaction.Mode, transaction.Date, orders.OrderType, transaction.Cashier,
                transaction.Discount, transaction.Waiter, transaction.Id FROM transaction 
                INNER JOIN orders ON transaction.OrderId = orders.Id 
                INNER JOIN user ON transaction.Member = user.Id 
                INNER JOIN member ON transaction.Member = member.UserId 
                INNER JOIN vendormember ON member.VendorId = vendormember.Id WHERE vendormember.UserId = 4 """)

        for row in cursor.fetchall():
            cashier = User.objects.filter(id=row[5])[0]
            waiter = User.objects.filter(id=row[7])[0]
            data.append([row[0], row[2], row[1], row[3], row[4], cashier.displayname, row[6],waiter.displayname,row[8]])
        context = {
            "Head": ["Customer Name", "Mode","Amount","Date","Order Type","Cashier Name","Discount","Waiter Name"],
            "Data": data,
        }
        return context

    def Get_TransetionDetials(self):
        try:
            userid = self.request.POST.get('select', "")
            data = []
            from django.db import connection
            cursor = connection.cursor()
            cursor.execute("""SELECT user.DisplayName, transaction.date, orders.OrderType, orders.Id, transaction.Discount, 
                                  transaction.Amount, transaction.Mode, transaction.Cashier, transaction.Waiter,
                                  transaction.Date FROM transaction 
                                  LEFT JOIN orders ON transaction.OrderId = orders.Id 
                                  LEFT JOIN user ON transaction.Member = user.Id 
                                  WHERE transaction.Id = """+userid)
            for row in cursor.fetchall():
                getitems = []
                cashier = User.objects.filter(id=row[7])[0]
                waiter = User.objects.filter(id=row[8])[0]
                print(row[3])
                items = Itemorder.objects.filter(oderid=row[3])
                for item in items:
                    getitems.append([item.itemname,item.itemprice,item.itemquantity,item.total])
                data.append([row[0], row[1], row[2], getitems, row[4], row[5], row[6],cashier.displayname ,waiter.displayname,row[9]])
            context = {
                "Data": data,
            }
            print(data)
            return context
        except Exception as error:
            print(str(error))

class Recharge():
    request = ""
    def __init__(self,req):
        self.request = req;

    def Get_Recharge_History(self):
        data = []
        recharge = RechargeHistory.objects.all()
        for row in recharge:
            if row.purpose != 'SMS':
                data.append([row.userid.userid,row.userid.displayname,row.date,row.type,row.amount,row.userid.balance,row.userid.expirydate])
        context = {
            "Head": ["Customer Id","Customer Name", "Recharge Date", "Recharge Type", "Recharge Amount","Balance","Expiry Date"],
            "Data": data,
        }
        return context

    def Vendor_Get_Recharge_History(self):
        data = []
        vendor = VendorMember.objects.get(userid=4)
        recharge = RechargeHistory.objects.filter(userid__member__vendor=vendor.id)
        for row in recharge:
            if row.purpose != 'SMS':
                data.append([row.userid.userid,row.userid.displayname,row.date,row.type,row.amount,row.userid.balance,row.userid.expirydate])
        context = {
            "Head": ["Customer Id","Customer Name", "Recharge Date", "Recharge Type", "Recharge Amount","Balance","Expiry Date"],
            "Data": data,
        }
        return context

    def Get_SMS_Recharge_History(self):
        data = []
        recharge = RechargeHistory.objects.all()
        for row in recharge:
            if row.purpose == 'SMS':
                data.append([row.userid.userid,row.userid.displayname,row.date,row.type,row.amount,row.userid.balance,row.userid.expirydate])
        context = {
            "Head": ["Vendor Id","Vendor Name", "Recharge Date", "Recharge Type", "Recharge Amount","Balance","Expiry Date"],
            "Data": data,
        }
        return context

class SearchRecords():
    request,todate,fromdate,searchval,type = '','','','',''

    def __init__(self,req):
        self.request = req
        self.todate = self.request.POST.get('todate', "")
        self.fromdate = self.request.POST.get('fromdate', "")
        self.searchval = self.request.POST.get('searchval', "")
        self.type = self.request.POST.get('type', "")

    def Get_Search_Data(self):
        data = []
        if(self.type == 'Vendors'):
            if(self.todate == "" and self.fromdate == "" and self.searchval != ""):
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status, vendor.BusinessName, vendor.BusinessEmail, vendor.BusinessContact, vendor.Industry, vendor.SystemName FROM user JOIN vendor ON user.Id = vendor.UserId  WHERE user.UserType= 'Vendors' AND user.Email LIKE '%" +self.searchval+"%' OR user.Mobile  LIKE '%"+self.searchval+"%' OR vendor.BusinessName LIKE '%"+self.searchval+"%' OR user.UserId LIKE '%"+self.searchval+"%' "
                data = self.Get_MYSQL_Data(sql)
                print(data)
            elif(self.todate != "" and self.fromdate != "" and self.searchval == ""):
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status, vendor.BusinessName, vendor.BusinessEmail, vendor.BusinessContact, vendor.Industry, vendor.SystemName FROM user JOIN vendor ON user.Id = vendor.UserId  WHERE user.UserType= 'Vendors' AND user.RegisterDate BETWEEN '"+self.todate+"' AND '"+self.fromdate+"'"
                data = self.Get_MYSQL_Data(sql)
                print(data)
            else:
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status, vendor.BusinessName, vendor.BusinessEmail, vendor.BusinessContact, vendor.Industry, vendor.SystemName FROM user JOIN vendor ON user.Id = vendor.UserId  WHERE user.UserType= 'Vendors' AND user.RegisterDate BETWEEN '"+self.todate+"' AND '"+self.fromdate+"' AND user.Email LIKE '%" + self.searchval + "%' OR user.Mobile  LIKE '%" + self.searchval + "%' OR vendor.BusinessName LIKE '%" + self.searchval + "%' OR user.UserId LIKE '%" + self.searchval + "%' "
                data = self.Get_MYSQL_Data(sql)
                print(data)
        elif self.type == 'Staff':
            if (self.todate == "" and self.fromdate == "" and self.searchval != ""):
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status,staff.Privilege, staff.Department FROM user JOIN staff ON user.Id = staff.UserId WHERE user.UserType= 'Staff' AND user.Mobile LIKE '%" + self.searchval + "%' OR user.DisplayName LIKE '%" + self.searchval + "%'"
                data = self.Get_MYSQL_Data(sql)
                print(data)
            elif (self.todate != "" and self.fromdate != "" and self.searchval == ""):
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status,staff.Privilege, staff.Department FROM user JOIN staff ON user.Id = staff.UserId WHERE user.UserType= 'Staff' AND user.RegisterDate BETWEEN '" + self.todate + "' AND '" + self.fromdate + "'"
                data = self.Get_MYSQL_Data(sql)
                print(data)
            else:
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status,staff.Privilege, staff.Department FROM user JOIN staff ON user.Id = staff.UserId WHERE user.UserType= 'Staff' AND user.RegisterDate BETWEEN '" + self.todate + "' AND '" + self.fromdate + "' AND user.Mobile LIKE '%"+self.searchval+"%' OR user.DisplayName LIKE '%"+self.searchval+"%'"
                data = self.Get_MYSQL_Data(sql)
                print(data)

        elif self.type == 'Members':
            if (self.todate == "" and self.fromdate == "" and self.searchval != ""):
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status,member.DateOfBirth, member.Gender FROM user JOIN member ON user.Id = member.UserId WHERE user.UserType= 'Members' AND user.Mobile LIKE '%" + self.searchval + "%' OR user.DisplayName LIKE '%" + self.searchval + "%' OR user.Email LIKE '%" + self.searchval + "%'  OR member.DateOfBirth LIKE '%" + self.searchval + "%'"
                data = self.Get_MYSQL_Data(sql)
                print(data)
            elif (self.todate != "" and self.fromdate != "" and self.searchval == ""):
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status,member.DateOfBirth, member.Gender FROM user JOIN member ON user.Id = member.UserId WHERE user.UserType= 'Members' AND user.RegisterDate BETWEEN '" + self.todate + "' AND '" + self.fromdate + "'"
                data = self.Get_MYSQL_Data(sql)
                print(data)
            else:
                sql = "SELECT user.UserId, user.DisplayName, user.Email, user.Mobile, user.RegisterDate, user.Status,member.DateOfBirth, member.Gender FROM user JOIN member ON user.Id = member.UserId WHERE user.UserType= 'Members' AND user.RegisterDate BETWEEN '" + self.todate + "' AND '" + self.fromdate + "' AND user.Mobile LIKE '%"+ self.searchval+"%' OR user.DisplayName LIKE '%"+ self.searchval+"%' OR user.Email LIKE '%"+ self.searchval +"%'  OR member.DateOfBirth LIKE '%" + self.searchval + ""
                data = self.Get_MYSQL_Data(sql)
                print(data)

        return data
    def Get_MYSQL_Data(self,sql):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(sql)
        for row in cursor.fetchall():
            temp = []
            for item in row:
                print(item)
                temp.append(str(item))
            data.append(temp)
            #data.append([row[0],row[1],row[2],row[3],str(row[4]),row[5],row[6],row[7],row[8],row[9],row[10]])

        return data

class CreateTable():
    request = ""

    def __init__(self,req):
        self.request = req

    def Get_Tables_Data(self):
        type = self.request.POST.get('tabletype',"")
        capacity = self.request.POST.get('tablecapacity',"")
        description = self.request.POST.get('tabledescription',"")
        user = User.objects.filter(id=25)[0]
        qr = QRCode([str(type),str(capacity),str(description)],user.userid)
        qrlink = qr.Create_QR_Code()
        Tables(tabletype=type,tablecapacity=capacity,tabledescription=description,availible="Yes",userid=user,qrcode= qrlink).save()
        return self.Tables_View()


    def Tables_View(self):
        data = []
        tables = Tables.objects.filter(userid=25).order_by('-userid__lastupdateddate')
        for table in tables:
            data.append([table.id,table.userid.displayname,table.tabletype,table.tabledescription,table.availible,table.tablecapacity])
        context = {
            "Title": "Tables",
            "Head": ["Id", "Name","Type","Details","Avalibilty","Capacity"],
            "Data": data,
        }
        return context

    def Get_Update_Table(self):
        userid = self.request.POST.get('select',"")
        table = Tables.objects.filter(id=userid)[0]
        data = [table.id,table.tabletype,table.tablecapacity,table.tabledescription,table.availible]
        return {"Data": data}

    def Update_Table_Data(self):
        id = self.request.POST.get('id',"")
        type = self.request.POST.get('tabletype',"")
        capacity = self.request.POST.get('tablecapacity',"")
        description = self.request.POST.get('tabledescription',"")
        avalibility = self.request.POST.get('avalibility',"")
        Tables.objects.filter(id= id).update(tabletype=type,tablecapacity=capacity,tabledescription=description,availible=avalibility)
        return self.Tables_View()

    def Delete_Table_Data(self):
        id = self.request.POST.get('id',"")
        Tables.objects.filter(id= id).delete()
        return self.Tables_View()

    def Book_Table(self):
        data = []
        tables = Tables.objects.filter(userid=25)
        for table in tables:
            data.append([table.tabletype,table.tablecapacity,table.tabledescription[:150] + '..',table.availible,table.id])
        return {
            "Data" : data
        }
    def Get_Table_Data(self,id):
        table = Tables.objects.filter(id = id)[0]
        return {"Data": [table.tabletype,table.tablecapacity,table.tabledescription,table.availible,id]}

    def Confirm_Booking(self):
        if self.request.method == 'POST':
            id = self.request.POST.get('id',"")
            bookingtime = self.request.POST.get('bookingdate',"")
            bookingtime = datetime.datetime.strptime(bookingtime,'%d %B %Y - %H:%M')
            table = Tables.objects.filter(id=id)[0]
            Booking(datetime=bookingtime,status="True",tableid=table,userid=table.userid).save()
            return {"Message" : "Success"}

class QRCode():
    data,userId ='',''
    def __init__(self,data,userid):
        self.data = data
        self.userId = userid

    def Create_QR_Code(self):
        # Create qr code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        # The data that you want to store
        data = self.data
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        qrcodename = 'QR'+str(self.userId)
        qrcodepath = os.path.join(BASE_DIR,'unltd/static/QR_Codes/')
        print(int(Tables.objects.latest('id').id))
        img.save(qrcodepath+"_"+qrcodename+"_"+self.data[0]+str(int(Tables.objects.latest('id').id)+ 1)+".jpg")
        return "QR_Codes/"+qrcodename+"image.jpg"

class GetItems():
    request = ''

    def __init__(self,req):
        self.request = req

    def Get_Items_For_Menu(self):
        userid = self.request.POST.get('select', "")
        data = []
        subcategories = Subcategory.objects.filter(categoryid__userid=4)
        for subcategory in subcategories:
            retriveItem = []
            items = Item.objects.filter(subcategoryid=subcategory.id)
            for item in items:
                retriveItem.append([item.itemname,item.itemimage,100,subcategory.subcategoryname.replace(" ","")+"-"+str(item.id)])
            data.append([subcategory.subcategoryname,retriveItem])

        return {"User":userid,"Data":data}

    def Get_Item_Variations(self):
        if self.request.method == "POST":
            data = []
            id = self.request.POST.get('id',"")
            id = id.split('-')
            variation = ItemVariation.objects.filter(itemid=id[1])
            for subItem in variation:
                data.append([subItem.id,subItem.title,subItem.price,subItem.discount])

            return {"Data":data}

    def Get_Ordered_Item_Details(self):
        data = []
        if self.request.method == 'POST':
            userid = self.request.POST.get('User', "")
            getOrderItems = self.request.POST.get('OrderItem',"")
            getOrderVariations = self.request.POST.get('OrderVariation',"")
            getOrderItems = getOrderItems.split(",")
            getOrderVariations = getOrderVariations.split(",")
            for element in getOrderItems:
                element = element.split("-")
                for variation in getOrderVariations:
                    items = ItemVariation.objects.filter(id=variation,itemid=element[1])
                    for item in items:
                        data.append([item.id,item.itemid.itemname,item.description,item.title,item.price,item.discount])
            return {"User": userid, "Data": data}

    def Confirm_orders(self):
        if (self.request.method == "POST"):
            orderitems,total,discount,prepareTime = [],0,0,0
            user = self.request.POST.get('User', "")
            print(user)
            for id in self.request.POST.getlist("ItemId[]"):
                quantity = self.request.POST.get(id, '')
                item = ItemVariation.objects.get(id=id)
                orderitems.append([item.itemid.itemname,item.title,item.price,quantity,float(item.price)*float(quantity)])
                discount+= ((float(item.price)*float(quantity)) / 100) * item.discount
                total+= (float(item.price)*float(quantity))
                if(item.itemid.preparetime > prepareTime): prepareTime = item.itemid.preparetime

            total = total - discount
            vendor= Venderorders.objects.get(userid=4)
            if(vendor == None):
                user = User.objects.get(id=4)
                vendor = Venderorders(userid=user).save()

            member = User.objects.get(userid=user)
            Orders(paymentstatus="Pending",ordertype="OrderbyStaff",totaltime=prepareTime,totalamount=total,vendorid=vendor,memberid=member,discount=discount).save()
            neworderid = Orders.objects.latest('id')
            for item in orderitems:
                Itemorder(itemname=item[0],itemvariation=item[1],itemprice=item[2],itemquantity=item[3],total=item[4],oderid = neworderid).save()
            user = UserViews(self.request)
            return user.Member_View()


