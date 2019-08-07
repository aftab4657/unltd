from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import  csv
from django.template import loader
from django.urls import reverse

from unltd.DBBackup.unltdbackupfile import Unltdbackup
from unltd.Settings.Settings import Setups
from .userviews.ViewData import UserViews, MailSend, GetData, UpdateUsers, UpdatePassword, UpdateStatus, Subscription, \
    Transaction, Recharge, SearchRecords, CreateTable, GetItems
from .userviews.VendorDiscount import Discount

from django.shortcuts import render
from unltd.createcategories.CreateCategories import EditCategories, CreateCategories
from unltd.createpackages.ViewPackages import FetchGenralSettings, ViewPackages
from unltd.items.item import EditItems, AddItems
from unltd.super_admin.TutorialData import TutorialView
from unltd.tickets.addtickets import ShowUnreadMessages, UploadFile, AddReply, ShowUpdatedMessages, ShowMessages, AddTickets, ViewTickets
from .createpackages.Createpackage import CreatePackage,EditPackages
from .smspackages.CreateSMSpackage import CreateSMSPackage,EditSMSPackages
from .smspackages.ViewSMSPackages import ViewSMSPackages
from .Signup.process import Validation
from .Signup.signup import Registration
from django.contrib import  messages
from .CreateGroup.create_group import CreateGroup
from .BroadCastEventMessages.BroadCastEventMessages import BroadCastEventMsg
from django.contrib.messages import constants as message_constants
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import translation
from django.views.decorators.csrf import csrf_exempt
from .user_signin.user_signin import UserAuthenticate
import json

@csrf_exempt
# Create your views here.
def Index_Translate(request):
    # if this is a POST request we need to switch the language
    if request.method == 'POST':
        print("ammar")
        request = switch_language(request)
    # if a GET (or any other method) we'll generate the page in English
    else:
        request.session[LANGUAGE_SESSION_KEY] = "en"
        translation.activate("en")

    return render(request, "packages/pricing_table.html")
# LANGUAGE SWITCHER

def switch_language(request):
    if request.session.has_key('username'):
        if request.session[LANGUAGE_SESSION_KEY] == "tl":
            request.session[LANGUAGE_SESSION_KEY] = "en"
            translation.activate("en")
            print("ammar2")
        elif request.session[LANGUAGE_SESSION_KEY] == "en":
            print("ammar3")
            request.session[LANGUAGE_SESSION_KEY] = "tl"
            translation.activate("tl")
        return request
    else:
        return HttpResponseRedirect('/unltd/login/')

# LANGUAGE SWITHCER END

def index(request):
    if request.session.has_key('username'):
        template = loader.get_template("index.html")
        context = {
            "Data": "",
            "Session":request
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def View_Vendor(request):
    if request.session.has_key('username'):
        request.session['Active'] = "ViewVendor"
        vendor = UserViews(request)
        context = vendor.Vendor_View()
        template = loader.get_template("vendormanagement/Views.html")
        print(request.session['Active'])
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def View_Staff(request):
    if request.session.has_key('username'):
        vendor = UserViews(request)
        context = vendor.Staff_View()
        template = loader.get_template("vendormanagement/Views.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def View_Member(request):
    if request.session.has_key('username'):
        vendor = UserViews(request)
        context = vendor.Member_View()
        template = loader.get_template("vendormanagement/Views.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Contact_Vendor(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            view = UserViews(request)
            email,contact = view.Return_Record()
            print(email)
            print(contact)
            template = loader.get_template("vendormanagement/contactvendor.html")
            context = {
                "userid" : request.POST.get('select',""),
                "email": email,
                "message" : contact,
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')


def Send_Message(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            type = request.POST.get('MessageType',"")
            body = request.POST.get('body',"")
            body = (str(body)).replace("<p>","").replace("</p>","")
            userid = request.POST.get('userid',"")
            if type == 'email':
                email = MailSend(request.POST.get('emailid',""),request.POST.get('subject',""),body,userid,
                                 request.POST.get('contact',""))
                msg = email.Send_Email()

            elif type == 'sms':
                email = MailSend(request.POST.get('emailid', ""), request.POST.get('subject', ""), body, userid,
                                 request.POST.get('contact', ""))
                msg = email.Send_SMS()


            context = {
                "message": msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return  HttpResponseRedirect('/unltd/login/')
def Update_Information(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            data = GetData(request)
            page,user = data.Get_Data_And_Template()
            template = loader.get_template(page)
            context = {
                "Data": user,
            }
            return HttpResponse(template.render(context, request))
    else:
        return  HttpResponseRedirect('/unltd/login/')

def Update_Vendor(request):
    if request.session.has_key('username'):
        vendor = UpdateUsers(request)
        vendor.Update_Vendor()
        vendor = UserViews(request)
        context = vendor.Vendor_View()
        template = loader.get_template("vendormanagement/Views.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Update_Staff(request):
    if request.session.has_key('username'):
        staff = UpdateUsers(request)
        staff.Update_Staff()
        vendor = UserViews(request)
        context = vendor.Staff_View()
        template = loader.get_template("vendormanagement/Views.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
def Update_Member(request):
    if request.session.has_key('username'):
        member = UpdateUsers(request)
        member.Update_Member()
        vendor = UserViews(request)
        context = vendor.Member_View()
        template = loader.get_template("vendormanagement/Views.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Load_Update_Password(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            template = loader.get_template("vendormanagement/UpdatePassword.html")
            context = {
                'userid': request.POST.get('select',"")
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Update_Password(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            password =UpdatePassword(request)
            context = password.Update_Password()
            template = loader.get_template("vendormanagement/Views.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Load_Update_Status(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            template = loader.get_template("vendormanagement/UpdateStatus.html")
            context = {
                'userid': request.POST.get('select', "")
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Update_Status(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            status =UpdateStatus(request)
            context = status.Updates_Status()
            template = loader.get_template("vendormanagement/Views.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Subscriptions(request):
    if request.session.has_key('username'):
        template = loader.get_template("vendormanagement/Subscription.html")
        subscribe = Subscription(request)
        context = subscribe.Get_Subscription_Invoices()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def SMSSubscriptions(request):
    if request.session.has_key('username'):
        template = loader.get_template("vendormanagement/Subscription.html")
        subscribe = Subscription(request)
        context = subscribe.Get_SMSSubscription_Invoices()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Transactions(request):
    if request.session.has_key('username'):
        template = loader.get_template("vendormanagement/Transactions.html")
        transect = Transaction(request)
        context = transect.Get_Transaction_Info()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def TransactionDetails(request):
    if request.session.has_key('username'):
        template = loader.get_template("vendormanagement/TransactionsDetails.html")
        transect = Transaction(request)
        context = transect.Get_TransetionDetials()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
def RechargeHistory(request):
    if request.session.has_key('username'):
        template = loader.get_template("vendormanagement/RechargeHistory.html")
        transect = Recharge(request)
        context = transect.Get_Recharge_History()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
def SMSCreditRecharge(request):
    if request.session.has_key('username'):
        template = loader.get_template("vendormanagement/RechargeHistory.html")
        transect = Recharge(request)
        context = transect.Get_SMS_Recharge_History()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Search(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            search = SearchRecords(request)
            data = search.Get_Search_Data()
            context = {
                "message": "seccuss",
                "Data": data
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login')

def LoadCreateTable(request):
    if request.session.has_key('username'):
        context = {
            "message": "seccuss",
        }
        template = loader.get_template("vendormanagement/CreateTable.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def GetCreateTable(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            table = CreateTable(request)
            context = table.Get_Tables_Data()
            template = loader.get_template("vendormanagement/Views.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Load_Tables_Data(request):
    if request.session.has_key('username'):
        tabble = CreateTable(request)
        context = tabble.Tables_View()
        template = loader.get_template("vendormanagement/Viewstables.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Load_Update_Tables(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            tabble = CreateTable(request)
            context = tabble.Get_Update_Table()
            template = loader.get_template("vendormanagement/UpdateTable.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
def Update_Tables(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            tabble = CreateTable(request)
            context = tabble.Update_Table_Data()
            template = loader.get_template("vendormanagement/Views.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Delete_Tables(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            tabble = CreateTable(request)
            context = tabble.Delete_Table_Data()
            template = loader.get_template("vendormanagement/Views.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Book_Tables(request):
    if request.session.has_key('username'):
        table = CreateTable(request)
        context = table.Book_Table()
        print(context)
        template = loader.get_template("vendormanagement/Booking.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Load_Booking_Details(request,id):
    if request.session.has_key('username'):
        table = CreateTable(request)
        context = table.Get_Table_Data(id)
        template = loader.get_template("vendormanagement/BookingDetails.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Confirm_BookTable(request):
    if request.session.has_key('username'):
        table = CreateTable(request)
        context = table.Confirm_Booking()
        template = loader.get_template("vendormanagement/Menu.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def View_Menu(request):
    if request.session.has_key('username'):
        item = GetItems(request)
        context = item.Get_Items_For_Menu()
        template = loader.get_template("vendormanagement/Menu.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
def Load_Order_Details(request):
    if request.session.has_key('username'):
        item = GetItems(request)
        context = item.Get_Ordered_Item_Details()
        print(context)
        template = loader.get_template("vendormanagement/LoadOrderDetails.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Get_Order(request):
    if request.session.has_key('username'):
        item = GetItems(request)
        context = item.Confirm_orders()
        template = loader.get_template("vendormanagement/Views.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Load_Variations(request):
    if request.session.has_key('username'):
        item = GetItems(request)
        context = item.Get_Item_Variations()
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login')


def Create_Packages(request):
    if request.session.has_key('username'):
        msg=''
        if request.method == "POST":
            obj=CreatePackage(request)
            msg=obj.Create_packages()
            context = {
                "Data":msg,
                "Settings": request.session['currency'],
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:


            data =  [['', '', '', '',
                      '','package_creation()','Save Button','']]

            context = {
                "Data": data,
                "Options": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                "Settings": request.session['currency'],

            }
            template = loader.get_template("packages/CreatePackages.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def View_Packages(request):
    if request.session.has_key('username'):
        packages = ViewPackages(request)
        context = packages.View_Packages()
        template = loader.get_template("packages/viewpackage.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
def Edit_Packages(request):
    if request.session.has_key('username'):
        if( request.method=='POST'):
            packageId=(request.POST.get('pkgID',""))
            obj = EditPackages(request,packageId)
            context=obj.Packgae_Edit()
        template = loader.get_template("packages/CreatePackages.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')


def Package_Editing(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            obj = EditPackages(request,'')
            msg=obj.Editing_Package()
            context = {
                "Data":msg,
            }
            print(msg)
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login')

def Delete_Packages(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            packageId = (request.POST.get('pkgID',""))
            obj = EditPackages(request, packageId)
            msg = obj.Delete()
            return  HttpResponseRedirect('/unltd/viewpackages')
    else:
        return HttpResponseRedirect('/unltd/login')


def Create_SMSPackages(request):
    if request.session.has_key('username'):
        msg=''
        if request.method == "POST":
            obj=CreateSMSPackage(request)
            msg=obj.Create_SMSpackages()
            context = {
                "Data": msg,
                "Settings": request.session['currency'],
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            data =  [['', '', '', '',
                     '','SMSpackage_creation()','Save Button','']]
            context = {
                "Data": data,
                "Options": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                "Settings": request.session['currency'],
            }
            template = loader.get_template("smspackages/CreateSMSPackages.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def View_SMSPackages(request):
    if request.session.has_key('username'):
        packages = ViewSMSPackages(request)
        context = packages.View_SMSPackages()
        print(context)
        template = loader.get_template("smspackages/ViewSMSPackages.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Edit_SMSPackages(request):
    if request.session.has_key('username'):
        if( request.method=='POST'):
            packageId=(request.POST.get('pkgID',""))
            obj = EditSMSPackages(request,packageId)
            context=obj.Packgae_SMSEdit()
        template = loader.get_template("smspackages/CreateSMSPackages.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Package_SMSEditing(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            obj = EditSMSPackages(request,'')
            msg=obj.Editing_PackageSMS()
            context = {
                "Data":msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login')

def Delete_SMSPackages(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            packageId = (request.POST.get('pkgID',""))
            obj = EditSMSPackages(request, packageId)
            msg = obj.SMSDelete()
            packages = ViewSMSPackages(request)
            context = packages.View_SMSPackages()
            return HttpResponseRedirect('/unltd/viewsmspackages')
    else:
        return HttpResponseRedirect('/unltd/login')

def Send_Message(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            type = request.POST.get('MessageType',"")
            body = request.POST.get('body',"")
            body = (str(body)).replace("<p>","").replace("</p>","")
            userid = request.POST.get('userid',"")
            if type == 'email':
                email = MailSend(request.POST.get('emailid',""),request.POST.get('subject',""),body,userid,
                                 request.POST.get('contact',""))
                msg = email.Send_Email()
            elif type == 'sms':
                email = MailSend(request.POST.get('emailid', ""), request.POST.get('subject', ""), body, userid,
                                 request.POST.get('contact', ""))
                msg = email.Send_SMS()
            context = {
                "message": msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login/')
def Update_Information(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            data = GetData(request)
            page,vendor = data.Get_Data_And_Template()
            template = loader.get_template(page)
            context = {
                "Data": vendor,
            }
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

# CREEATE VENDER MEMEBER STAFF START

def Vendor_Signup(request):
    if request.session.has_key('username'):
        template = loader.get_template("create_vender_member_staff/createvendor.html")
        context = {
            "Data": "",
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
def Member_Signup(request):
    if request.session.has_key('username'):
        template = loader.get_template("create_vender_member_staff/createmember.html")
        context = {
            "Data": "",
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def staff_Signup(request):
    if request.session.has_key('username'):
        template = loader.get_template("create_vender_member_staff/createstaff.html")
        context = {
            "Data": "",
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

def Validations(request):
    if request.session.has_key('username'):
        obj = Validation(request)
        if(request.method=='POST'):
            res = obj.Email_Check()
        return HttpResponse(res)
    else:
        return HttpResponseRedirect('/unltd/login')

#Creating Accounts
def CreateAccounts(request):
    if request.session.has_key('username'):
        obj = Registration(request)
        if (request.method == 'POST'):
            if request.POST.get('user') == 'Vendor':
                msg = obj.Vendor_Signup()
                if (msg == 'Saved'):
                    messages.success(request, 'Account Created Successfully!', extra_tags='alert-success fa-smile-o')
                else:
                    messages.success(request, 'There is problem please try again!', extra_tags='alert-danger fa-frown-o')
                HttpResponseRedirect('vendorsignup')
            if request.POST.get('user') == 'Member':
                msg = obj.Member_Signup()
            if request.POST.get('user') == 'Staff':
                msg = obj.Staff_Signup()
        return HttpResponse(msg)
    else:
        return HttpResponseRedirect('/unltd/login')
# CREATE VENDER MEMBER STAFF END
# vendor profile
def Vendor_Profile(request):
    if request.session.has_key('username'):
        template = loader.get_template("ProfilesManagement/VendorProfile.html")
        context = {
            "Data": "",
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
# Personal profiles

def Personal_Profile(request):
    if request.session.has_key('username'):
         if(request.method=='POST'):
            d=GetData(request)
            d.Get_PUData_And_Template()
         data = GetData(request)
         page, profile = data.Get_PData_And_Template()
         template = loader.get_template(page)
         context = {
             "Data": profile,
         }
         return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')
#password change
def Settings_Profile(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            d = GetData(request)
            msg =  d.Update_Profile_Password()
            if(msg=='Success'):
                messages.success(request, 'Settings Updated Successfully!', extra_tags='alert-success fa-smile-o')
            else:
                messages.success(request, 'There is problem please try again!', extra_tags='alert-danger fa-frown-o')
            return HttpResponseRedirect('profileSettings')
        template = loader.get_template("ProfilesManagement/ProfilesSetting.html")
        context = {
            "Data": "",
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login')

#password check

def PValidations(request):
    if request.session.has_key('username'):
        if(request.method=='POST'):
            request.session['id'] = "1"
            obj = Validation(request)
            res = obj.password_Check()
        return HttpResponse(res)
    else:
        return HttpResponseRedirect('/unltd/login')
# End Password validation Danian Code END

# CREATE GROUP

def create_group(request):
    if request.session.has_key('username'):
        create_group_obj = CreateGroup(request)
        data = create_group_obj.get_all_members_with_group_by()
        print(data["Data"])
        vender_list = []
        member_list = []
        staff_list = []
        for i in data["Data"]:
            if i[2].lower() == "member":
                member_list.append(i)
            elif i[2].lower() == "staff":
                staff_list.append(i)
            elif i[2].lower() == "vendeor":
                vender_list.append(i)
        # group = {"Vendors": vender_list, "Staff": staff_list, "Members": member_list}
        # print(group)
        template = loader.get_template("group/create_group.html")
        context = {
            "Vendors": vender_list,
            "Staff": staff_list,
            "Members": member_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def creategroup_action(request):
    if request.session.has_key('username'):
        print(request.POST)
        if "GET" == request.method:
            return HttpResponseRedirect('creategroup/')
        # if not GET, then proceed
        try:
            create_group_obj = CreateGroup(request)
            check = create_group_obj.Create_Group()
            if check == 1:
                print('success')
                messages.success(request, 'Group Created Successfully!', extra_tags='alert-success fa-smile-o')
                return HttpResponseRedirect('creategroup/')
            elif check == 0:
                messages.success(request, 'There is Problem Please Try again!', extra_tags='alert-danger fa-frown-o')
                return HttpResponseRedirect('creategroup/')
            elif check == -1:
                print('Choose Members')
                messages.success(request, 'Please choose Group Members!', extra_tags='alert-danger fa-frown-o')
                return HttpResponseRedirect('creategroup/')
        except Exception as e:
            print(e)
            messages.success(request, 'Something went wrong Please Try again!', extra_tags='alert-danger fa-frown-o')
            return HttpResponseRedirect('creategroup/')
    else:
        return HttpResponseRedirect('/unltd/login/')

# MESSSAGES

def create_message_template(request):
    if request.session.has_key('username'):
        template = loader.get_template("messages/broadcast_messages/sms.html")
        all_groups_obj = CreateGroup(request)
        all_groups = all_groups_obj.get_all_groups()
        context = {
            "Data": all_groups["Data"],
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def create_email_template(request):
    if request.session.has_key('username'):
        template = loader.get_template("messages/broadcast_messages/email.html")
        all_groups_obj = CreateGroup(request)
        all_groups = all_groups_obj.get_all_groups()
        context = {
            "Data": all_groups["Data"],
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def create_event_message_template(request):
    if request.session.has_key('username'):
        template = loader.get_template("messages/event_messages/sms.html")
        context = {
            "Data": "",
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def create_event_email_template(request):
    if request.session.has_key('username'):
        template = loader.get_template("messages/event_messages/email.html")
        context = {
            "Data": "",
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def sendsms(request):
    if request.session.has_key('username'):
        msg_obj = BroadCastEventMsg(request)
        check = msg_obj.SendSMS()
        print(request.POST.get('group'))
        if check == 1:
            print('success')
            messages.success(request, 'SMS Sent!', extra_tags='alert-success fa-smile-o')
        elif check == 2:
            print('success')
            messages.success(request, 'SMS Saved in Draft!', extra_tags='alert-success fa-smile-o')
        else:
            messages.success(request, 'SMS not  Sent Please try again! ', extra_tags='alert-danger fa-frown-o')
        return HttpResponseRedirect('/unltd/create_sms/')
    else:
        return HttpResponseRedirect('/unltd/login/')

#admin and vendor conversation/chat
def View_Tickets(request):
    if request.session.has_key('username'):
        tickets = ViewTickets(request)
        context = tickets.View_Tickets()
        template = loader.get_template("tickets/viewtickets.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Add_Ticket(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            obj = AddTickets(request)
            msg = obj.Add_Tickets()
            if msg:
                messages.success(request, 'Ticket Created Successfully!', extra_tags='alert-success fa-smile-o')
                return HttpResponseRedirect('/unltd/viewtutorial/')
            else:
                messages.success(request, 'Error in Creating Ticket! Try Again',  extra_tags='alert-danger fa-frown-o')
                return HttpResponseRedirect('/unltd/addtutorial')
        else:
            context = {
                "Data": 'msg',
            }
            template = loader.get_template("tickets/addticket.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Show_Conversation(request,id):
    if request.session.has_key('username'):
        obj = ShowMessages(request, id)
        context = obj.Show_Messages()
        template = loader.get_template("tickets/conversation.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Reply_Timer(request):
    if request.session.has_key('username'):
        id = (request.POST.get('id'))
        lastid = (request.POST.get('lastid'))
        print(lastid)
        obj = ShowUpdatedMessages(request, id,lastid)
        records = obj.Show_UpdatedMessages()
        records=json.dumps(records, indent=4, sort_keys=True, default=str)
        return HttpResponse(records, content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login/')

def Reply_Conversation(request):
    if request.session.has_key('username'):
        obj = AddReply(request)
        msg = obj.Add_Reply()
        if msg:
            context = {
                "Data": msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login/')

def Upload_Form(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            obj = UploadFile(request)
            context = obj.Upload_File()
            if context[0]=='ERROR':
                messages.success(request, 'Please enter your message!', extra_tags='alert-danger fa-frown-o')
                template = loader.get_template("tickets/conversation.html")
                return HttpResponse(template.render(context[1], request))
            else:
                messages.success(request, 'Message Sent', extra_tags='alert-success fa-smile-o')
                template = loader.get_template("tickets/conversation.html")
                return HttpResponse(template.render(context[1], request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Unread_Message(request):
    if request.session.has_key('username'):
        obj = ShowUnreadMessages(request)
        context = obj.Show_Unread_Messages()
        context = json.dumps(context, indent=4, sort_keys=True, default=str)
        print(context)
        return HttpResponse(context, content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login/')
   #create categories/subcategories view.py
def Create_Categories(request):
    if request.session.has_key('username'):
        msg=''
        if request.method == "POST":
            obj=CreateCategories(request)
            msg=obj.Create_Categories()
            context = {
                "Data":msg,
            }
            print(context)
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            data = [['', '', 'Categories_Creation()', 'Save Button', '']]

            context = {
                "Data": data,"Options": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            }
            template = loader.get_template("categories_subcategories/createcategories.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Create_SubCategories(request):
    if request.session.has_key('username'):
        msg=''
        if request.method == "POST":
            obj = CreateCategories(request)
            msg = obj.Create_SubCategories()
            context = {
                "Data":msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            obj = CreateCategories(request)
            msg = obj.Fetch_Categories()
            data =  [['', '','','SubCategories_Creation()','Save Button','']]
            context = {"Data": data,"Records":msg,"Options": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']}
            template = loader.get_template("categories_subcategories/createsubcategories.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def View_Categories(request):
    if request.session.has_key('username'):
        packages = CreateCategories(request)
        context = packages.View_Categories()
        template = loader.get_template("categories_subcategories/viewcategories.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Edit_Categories(request):
    if request.session.has_key('username'):
        if( request.method=='POST'):
            packageId=(request.POST.get('select',""))
            obj = EditCategories(request,packageId)
            msg=obj.Edit_Categories()
            context = {"Data": msg,"Options": ['1','2','3','4','5','6','7','8','9','10','11','12']}
            template = loader.get_template("categories_subcategories/createcategories.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Editing_Category(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            obj = EditCategories(request,'')
            msg=obj.Editing_Categoryy()
            context = {
                "Data":msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login/')


def Delete_Categories(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            packageId = (request.POST.get('select',""))
            obj = EditCategories(request, packageId)
            msg = obj.Category_Delete()
            return HttpResponseRedirect('/unltd/viewcategories/')
    else:
        return HttpResponseRedirect('/unltd/login/')

def View_SubCategories(request):
    if request.session.has_key('username'):
        packages = CreateCategories(request)
        context = packages.View_SubCategories()
        template = loader.get_template("categories_subcategories/viewsubcategories.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Edit_SubCategories(request):
    if request.session.has_key('username'):
        if( request.method=='POST'):
            packageId=(request.POST.get('select',""))
            obj = EditCategories(request,packageId)
            context=obj.Edit_SubCategories()
            template = loader.get_template("categories_subcategories/createsubcategories.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Editing_SubCategory(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            obj = EditCategories(request,'')
            msg=obj.Editing_SubCategoryy()
            context = {
                "Data": msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponseRedirect('/unltd/login/')

def Delete_SubCategories(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            packageId = (request.POST.get('select',""))
            obj = EditCategories(request, packageId)
            msg = obj.SubCategory_Delete()
            return HttpResponseRedirect('/unltd/viewsubcategories/')
    else:
        return HttpResponseRedirect('/unltd/login/')

#ADD items View
def Add_Items(request):
    if request.session.has_key('username'):
        msg=''
        if request.method == "POST":
            obj = AddItems(request)
            msg = obj.Add_Items()
            context = {
                "Data":msg,
                "Settings": request.session['currency'],
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            obj = AddItems(request)
            msg = obj.Fetch_SubCategories()

            data =  [['', '','','','','','','','','Add_Items()','Save Button','']]
            context = {"Data": data,
                       "Records":msg,
                       "Options": [['Yes', '1'],['No','0']]}
            template = loader.get_template("items/additems.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Upload_ItemsImage(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            obj = AddItems(request)
            context = obj.Add_ItemImage()
            print(context)
            if context==False:

                messages.success(request, 'Failed! Item not added.', extra_tags='alert-danger fa-frown-o')
                return HttpResponseRedirect('/unltd/additems/')
            else:
                messages.success(request, 'Item Added', extra_tags='alert-success fa-smile-o')
                return HttpResponseRedirect('/unltd/additems/')
    else:
        return HttpResponseRedirect('/unltd/login/')

def View_Items(request):
    if request.session.has_key('username'):
        packages = AddItems(request)
        context = packages.View_Items()
        template = loader.get_template("items/viewitems.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Delete_Items(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            packageId = (request.POST.get('select',""))
            obj = EditItems(request, packageId)
            msg = obj.Item_Delete()
            packages = AddItems(request)
            context = packages.View_Items()
            template = loader.get_template("items/viewitems.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Edit_Items(request):
    if request.session.has_key('username'):
        if( request.method=='POST'):
            packageId=(request.POST.get('select',""))
            obj = EditItems(request,packageId)
            context=obj.Edit_Items()
            template = loader.get_template("items/additems.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Editing_Items(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            packageId = (request.POST.get('select', ""))
            obj = EditItems(request,packageId)
            context = obj.Editing_Items()
            print(context)
            return HttpResponseRedirect('/unltd/viewitems/')
    else:
        return HttpResponseRedirect('/unltd/login/')
# tutorial views

def ShowCustomerTutorial(request):
    tutorial = TutorialView(request)
    context = tutorial.Show_Customer_Tutorial()
    template = loader.get_template("Tutorials/ShowTutorial.html")
    return HttpResponse(template.render(context, request))
def ShowVendorTutorial(request):
    tutorial = TutorialView(request)
    context = tutorial.Show_Vendor_Tutorial()
    template = loader.get_template("Tutorials/ShowTutorial.html")
    return HttpResponse(template.render(context, request))

def ShowTutorialDetail(request):
    tutorial = TutorialView(request)
    context = tutorial.Show_Tutorial_Detail(request)
    template = loader.get_template("Tutorials/AddTutorial.html")
    return HttpResponse(template.render(context, request))

def AddTutorial(request):
    vendor = TutorialView(request)
    template = loader.get_template("Tutorials/AddTutorial.html")
    if request.method == 'POST':
        if 'btnadd' in request.POST:
            msg = vendor.Add_Tutorial(request)
            if (msg == 'success'):
                messages.success(request, 'Tutorial Uploaded Successfully!', extra_tags='alert-success fa-smile-o')

            else:
                messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
        elif 'btnupdate' in request.POST:
            msg = vendor.Update_Tutorial(request)
            if (msg == 'success'):
                messages.success(request, 'Tutorial Updated Successfully!', extra_tags='alert-success fa-smile-o')

            else:
                messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')

        return HttpResponseRedirect(reverse('AddTutorial'))
    else:
        context=vendor.Show_Tutorial_Type()
        context["Title"]="Add Tutorial"
        return HttpResponse(template.render(context, request))

def EditTutorial(request):
    vendor = TutorialView(request)
    template = loader.get_template("Tutorials/AddTutorial.html")
    if request.method == 'POST':
        if 'btndelete' in request.POST:
            msg = vendor.Delete_Tutorial(request)
            if (msg == 'success'):
                messages.success(request, 'Tutorial Deleted Successfully!', extra_tags='alert-success fa-smile-o')

            else:
                messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
            return HttpResponseRedirect(reverse('ShowTutorial'))
        elif 'btnedit' in request.POST:
            print('I am btnedit')
            content = vendor.Edit_Tutorial(request)
        return HttpResponse(template.render(content, request))
    else:
        return HttpResponseRedirect(reverse('AddTutorial'))

def ShowBackup(request):
    db=Unltdbackup(request)
    context=db.Show_Backup()
    template = loader.get_template("DBBackup/Takebackup.html")
    db.Take_Backup
    return HttpResponse(template.render(context, request))

def TakeBackup(request):
    db=Unltdbackup(request)
    template = loader.get_template("DBBackup/Takebackup.html")
    if 'btndelete' in request.POST:
        msg = db.Delete_Backup(request)
        if (msg == 'success'):
            messages.success(request, 'Backup Deleted Successfully!', extra_tags='alert-success fa-smile-o')

        else:
            messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
        return HttpResponseRedirect(reverse('Showdbbackup'))

    else:
        print('I am btnedit')
        msg = db.Take_Backup()
        if (msg == 'success'):
            messages.success(request, 'Backup Created Successfully!', extra_tags='alert-success fa-smile-o')

        else:
            messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
        return HttpResponseRedirect(reverse('Showdbbackup'))

def AddTutorialType(request):
    type=TutorialView(request)
    template=loader.get_template("Tutorials/TutorialType.html")
    if 'btnadd' in request.POST:
        msg = type.Add_Tutorial_Type(request)
        if (msg == 'success'):
            messages.success(request, 'Tutorial Type Added Successfully!', extra_tags='alert-success fa-smile-o')

        else:
            messages.warning(request, msg, extra_tags='fa-frown-o alert-danger ')
        return HttpResponseRedirect(reverse('AddTutorialType'))

    elif 'btndelete' in request.POST:
        print('I am btndelete')
        msg = type.Delete_Tutorial_Type(request)
        if (msg == 'success'):
            messages.success(request, 'Tutorial Type Deleted Successfully!', extra_tags='alert-success fa-smile-o')

        else:
            messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
        return HttpResponseRedirect(reverse('AddTutorialType'))
    elif 'btnupdate' in request.POST:
        msg=type.Update_Tutorial_Type(request)
        if (msg == 'success'):
            messages.success(request, 'Tutorial Type Updated Successfully!', extra_tags='alert-success fa-smile-o')

        else:
            messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
        return HttpResponseRedirect(reverse('AddTutorialType'))
    elif request.is_ajax():
        print('I am btnedit')
        msg = type.Edit_Tutorial_Type(request)
        # context=type.Show_Tutorial_Type()
        return JsonResponse(msg)
    context=type.Show_Tutorial_Type()
    return HttpResponse(template.render(context,request))


#ADD items View
def Add_Items(request):
    if request.session.has_key('username'):
        msg=''
        if request.method == "POST":
            obj = AddItems(request)
            msg = obj.Add_Items()
            context = {
                "Data":msg,
                "Settings": request.session['currency'],
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            obj = AddItems(request)
            msg = obj.Fetch_SubCategories()
            data =  [['', '','','','','','','','Add_Items()','Save Button','','','']]
            context = {"Data": data,
                       "Records":msg,
                       "Options": [['Yes', '1'],['No','0']],
                       "Settings": request.session['currency'],
                       }
            template = loader.get_template("items/additems.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Upload_ItemsImage(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            obj = AddItems(request)
            context = obj.Add_ItemImage()
            print(context)
            if context==False:
                messages.success(request, 'Failed! Item not added.', extra_tags='alert-danger fa-frown-o')
                return HttpResponseRedirect('/unltd/additems/')
            else:
                messages.success(request, 'Item Added', extra_tags='alert-success fa-smile-o')
                return HttpResponseRedirect('/unltd/additems/')
    else:
        return HttpResponseRedirect('/unltd/login/')

def View_Items(request):
    if request.session.has_key('username'):
        packages = AddItems(request)
        context = packages.View_Items()
        print(context)
        template = loader.get_template("items/viewitems.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Delete_Items(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            packageId = (request.POST.get('select',""))
            obj = EditItems(request, packageId)
            print(packageId)
            msg = obj.Item_Delete()
            packages = AddItems(request)
            context = packages.View_Items()
            template = loader.get_template("items/viewitems.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Edit_Items(request):
    if request.session.has_key('username'):
        if( request.method=='POST'):
            packageId=(request.POST.get('select',""))
            obj = EditItems(request,packageId)
            context=obj.Edit_Items()
            template = loader.get_template("items/additems.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Editing_Items(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            packageId = (request.POST.get('select', ""))
            obj = EditItems(request,packageId)
            context = obj.Editing_Items()
            return HttpResponseRedirect('/unltd/viewitems/')
    else:
        return HttpResponseRedirect('/unltd/login/')





# USER Signin Template
def UserSignin(request):
    template = loader.get_template("user_signin/signin.html")
    context = {
        "Data": "",
    }
    return HttpResponse(template.render(context, request))

def UserSigninAuthenticattion(request):
    username = (request.POST.get('username'))
    password = (request.POST.get('password'))
    # if username == 'superadmin':
    #     spa_users = SuperAdmin(request)
    #     context = spa_users.SuperAdminAuthenticate()
    #     print(context['Data'])
    #     for u in context['Data']:
    #         if u[0] == username and u[1] == password:
    #             request.session['username'] = username
    #             return HttpResponseRedirect('/unltd/index/')
    # else:
    try:
        users = UserAuthenticate(request)
        user = users.UserAuth()
        print(user)
        request.session['username'] = user['Data'][0]['Email']
        request.session['id'] = user['Data'][0]['Id']
        request.session['UserType'] = user['Data'][0]['UserType']
        request.session['UserId'] = user['Data'][0]['UserId']
        request.session['DisplayName'] = user['Data'][0]['DisplayName']
        request.session['user_type'] = user['Data'][0]['UserType']
        obj2 = FetchGenralSettings(request)
        try:
            msg2 = obj2.Fetch_Settings()
            request.session['language']=msg2[0][0]
            request.session['currency'] = msg2[0][1]
        except Exception as e:
            request.session['language'] = 'English'
            request.session['currency'] = '$'
        print(request.session['id'])
        print(request.session['UserType'])


        return HttpResponseRedirect('/unltd/index/')
    except Exception as e:
        print(e)
    return HttpResponseRedirect('/unltd/login/')
def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponseRedirect('/unltd/login/')

#Create Backup
def ShowBackup(request):
    db=Unltdbackup(request)
    context=db.Show_Backup()
    template = loader.get_template("DBBackup/Takebackup.html")
    db.Take_Backup
    return HttpResponse(template.render(context, request))

def TakeBackup(request):
    db=Unltdbackup(request)
    template = loader.get_template("DBBackup/Takebackup.html")
    if 'btndelete' in request.POST:
        msg = db.Delete_Backup(request)
        if (msg == 'success'):
            messages.success(request, 'Backup Deleted Successfully!', extra_tags='alert-success fa-smile-o')

        else:
            messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
        return HttpResponseRedirect(reverse('Showdbbackup'))

    else:
        print('I am btnedit')
        msg = db.Take_Backup()
        if (msg == 'success'):
            messages.success(request, 'Backup Created Successfully!', extra_tags='alert-success fa-smile-o')

        else:
            messages.warning(request, 'There is problem please try again!', extra_tags='fa-frown-o alert-danger ')
        return HttpResponseRedirect(reverse('Showdbbackup'))



# VENDOR MANAGEMENT
def Load_Vendor_Index(request):
    context = {}
    template = loader.get_template("Vendor_Index.html")
    return HttpResponse(template.render(context, request))

def Load_Vendor_Staff(request):
    print("Jawad")
    staff = UserViews(request)
    context = staff.Vendor_Staff_View()
    template = loader.get_template("VendorSystem/VendorViews.html")
    return HttpResponse(template.render(context, request))

def Load_Vendor_Member(request):
    vendor = UserViews(request)
    context = vendor.Vendor_MemberView()
    template = loader.get_template("VendorSystem/VendorViews.html")
    return HttpResponse(template.render(context, request))

def Vendor_ContacForm(request):
    if request.method == "POST":
        view = UserViews(request)
        email,contact = view.Return_Record()
        print(email)
        print(contact)
        template = loader.get_template("VendorSystem/Vendor_ContactForm.html")
        context = {
            "userid" : request.POST.get('select',""),
            "email": email,
            "message" : contact,
        }
        return HttpResponse(template.render(context, request))

def Vendor_Update_Information(request):
    if request.method == "POST":
        data = GetData(request)
        page,user = data.Vendor_Get_Data_And_Template()
        template = loader.get_template(page)
        context = {
            "Data": user,
        }
        return HttpResponse(template.render(context, request))

def Vendor_Update_Staff(request):
    staff = UpdateUsers(request)
    staff.Update_Staff()
    vendor = UserViews(request)
    context = vendor.Vendor_Staff_View()
    template = loader.get_template("VendorSystem/VendorViews.html")
    return HttpResponse(template.render(context, request))

def Vendor_Update_Member(request):
    member = UpdateUsers(request)
    member.Update_Member()
    vendor = UserViews(request)
    context = vendor.Vendor_MemberView()
    template = loader.get_template("VendorSystem/VendorViews.html")
    return HttpResponse(template.render(context, request))

def Vendor_Load_Update_Password(request):
    if request.method == "POST":
        template = loader.get_template("VendorSystem/Vendor_UpdatePassword.html")
        context = {
            'userid': request.POST.get('select',"")
        }
        return HttpResponse(template.render(context, request))

def Vendor_Update_Password(request):
    if request.method == "POST":
        password =UpdatePassword(request)
        context = password.Vendor_Update_Password()
        template = loader.get_template("VendorSystem/VendorViews.html")
        return HttpResponse(template.render(context, request))

def Vendor_Load_Update_Status(request):
    if request.method == "POST":
        template = loader.get_template("VendorSystem/Vendor_UpdateStatus.html")
        context = {
            'userid': request.POST.get('select', "")
        }
        return HttpResponse(template.render(context, request))

def Vendor_Update_Status(request):
    if request.method == "POST":
        status =UpdateStatus(request)
        context = status.Vendor_Updates_Status()
        template = loader.get_template("VendorSystem/VendorViews.html")
        return HttpResponse(template.render(context, request))

def Vendor_Transactions(request):
    template = loader.get_template("VendorSystem/Vendor_Transactions.html")
    transect = Transaction(request)
    context = transect.Vendor_Get_Transaction_Info()
    return HttpResponse(template.render(context, request))

def Vendor_TransactionDetails(request):
    template = loader.get_template("VendorSystem/Vendor_TransactionsDetails.html")
    transect = Transaction(request)
    context = transect.Get_TransetionDetials()
    return HttpResponse(template.render(context, request))

def RechargeHistory(request):
    template = loader.get_template("VendorSystem/Vendor_RechargeHistory.html")
    transect = Recharge(request)
    context = transect.Vendor_Get_Recharge_History()
    return HttpResponse(template.render(context, request))

# END VENDOR

# ITEM OFFER
def Item_Offer(request):
    if request.session.has_key('username'):
        msg=''
        if request.method == "POST":
            Id = (request.POST.get('select', ""))
            context = {
                "Id":Id,
                "Settings": request.session['currency'],
                "Button": ["Add Offers", "Add_Offers ()"],

            }

            template = loader.get_template("items/additemoffer.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Creating_Offer(request):
    if request.session.has_key('username'):
        msg = ''
        if request.method == "POST":
            obj = AddItems(request)
            msg = obj.Add_offers()
            print(msg)
            context = {
                "Data": msg,
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            return HttpResponseRedirect('/unltd/viewitems/')
    else:
        return HttpResponseRedirect('/unltd/login/')

def View_Offer(request):
    if request.session.has_key('username'):
        obj = AddItems(request)
        context = obj.View_Offers()

        template = loader.get_template("items/viewoffers.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

def Delete_Offers(request):
    if request.session.has_key('username'):
        if (request.method == 'POST'):
            packageId = (request.POST.get('select',""))
            obj = EditItems(request, packageId)
            msg = obj.Offer_Delete()
            packages = AddItems(request)
            context = packages.View_Offers()
            template = loader.get_template("items/viewoffers.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Edit_Offers(request):
    if request.session.has_key('username'):
        if( request.method=='POST'):
            packageId=(request.POST.get('select',""))
            obj = EditItems(request,packageId)
            context=obj.Edit_Offer()
            template = loader.get_template("items/additemoffer.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')
def Editing_Offers(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            packageId = (request.POST.get('select', ""))
            obj = EditItems(request,packageId)
            context = obj.Editing_Offers()
            packages = AddItems(request)
            context = packages.View_Offers()
            template = loader.get_template("items/viewoffers.html")
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/unltd/login/')

# VENDOR SICOUNT


def Load_CreateDiscount(request):
    template = loader.get_template("Discount/CreateDiscount.html")
    context = {"Head" : "Create"}
    return HttpResponse(template.render(context, request))

def CreateDiscount(request):
    template = loader.get_template("Discount/ViewDiscounts.html")
    discount = Discount(request)
    context = discount.Create_Discount('create')
    return HttpResponse(template.render(context, request))

def ViewDiscount(request):
    template = loader.get_template("Discount/ViewDiscounts.html")
    discount = Discount(request)
    data = discount.Get_Discounts()
    context = { "Head": ["Id","Title","DiscountType","Discount","CreatedDate","ExpiryDate"],
                     "Data": data}
    return HttpResponse(template.render(context, request))

def Load_DiscountUpdateDelete(request):
    template = loader.get_template("Discount/CreateDiscount.html")
    discount = Discount(request)
    context = discount.Get_DiscountData()
    return HttpResponse(template.render(context, request))

def UpdateDiscount(request):
    template = loader.get_template("Discount/ViewDiscounts.html")
    discount = Discount(request)
    context = discount.Create_Discount('update')
    return HttpResponse(template.render(context, request))

def DeleteDiscount(request):
    template = loader.get_template("Discount/ViewDiscounts.html")
    discount = Discount(request)
    context = discount.Delete_Discount()
    return HttpResponse(template.render(context, request))



# DANIYAN START SETTING

def SMS_Setup(request):
    obj = Setups(request)
    if(request.method == 'POST'):
        res = obj.Sms_Setup()
        if (res == 'Saved'):
            messages.success(request,'Successfully Saved!', extra_tags='alert-success fa-smile-o')
        else:
            messages.success(request, res, extra_tags='alert-danger fa-frown-o')
        return HttpResponseRedirect("/unltd/sms_setup/")
    page, pdata = obj.Details_Sms()
    template = loader.get_template(page)
    context = {
        "Data": pdata,
    }
    return HttpResponse(template.render(context, request))

def google_Setup(request):
    obj = Setups(request)
    if (request.method == 'POST'):

        res = obj.Google_Setup()
        if (res == 'Saved'):
            messages.success(request,'Successfully Saved!', extra_tags='alert-success fa-smile-o')
        else:
            messages.success(request, res, extra_tags='alert-danger fa-frown-o')
        return HttpResponseRedirect("/unltd/google_Setup/")
    page, pdata = obj.Details_Google()
    template = loader.get_template(page)
    context = {
        "Data": pdata,
    }
    return HttpResponse(template.render(context, request))

def payment_Gateway(request):
    obj = Setups(request)
    if (request.method == 'POST'):
        res = obj.payments_gateway()
        if (res == 'Saved'):
            messages.success(request, 'Successfully Saved!', extra_tags='alert-success fa-smile-o')
        else:
            messages.success(request, res, extra_tags='alert-danger fa-frown-o')
        return HttpResponseRedirect("/unltd/payment/")
    page, pdata = obj.Details_Bank()
    template = loader.get_template(page)
    context = {
        "Data": pdata,
    }
    return HttpResponse(template.render(context, request))

def paypal_Setup(request):
    obj = Setups(request)
    if (request.method == 'POST'):
        obj = Setups(request)
        res = obj.paypal_Setup()
        if (res == 'Saved' or res == 'Deleted'):
            messages.success(request, 'Successfully "'+str(res)+'"!', extra_tags='alert-success fa-smile-o')
        else:
            messages.success(request, res, extra_tags='alert-danger fa-frown-o')
        return HttpResponseRedirect("/unltd/paypal/")

    page, pdata = obj.Details_Paypal()
    template = loader.get_template(page)
    context = {
        "Head":["Email","Status"],
        "Data": pdata,
    }
    return HttpResponse(template.render(context, request))

def Strip_Setup(request):
    obj = Setups(request)
    if (request.method == 'POST'):
        obj = Setups(request)
        res = obj.strip_Setup()
        if (res == 'Saved' or res == 'Deleted'):
            messages.success(request, 'Successfully "'+str(res)+'"!', extra_tags='alert-success fa-smile-o')
        else:
            messages.success(request, res, extra_tags='alert-danger fa-frown-o')
        return HttpResponseRedirect("/unltd/strip/")

    page, pdata = obj.Details_strip()
    template = loader.get_template(page)
    context = {
        "Head":["Email","Status"],
        "Data": pdata,
    }
    return HttpResponse(template.render(context, request))

# Danian Code END




