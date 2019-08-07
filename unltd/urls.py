from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url('translate/', views.Index_Translate, name='translate'),

    path('index/', views.index, name= 'index'),
    path('viewvendor/', views.View_Vendor, name = 'viewvendor'),
    path('viewstaff/', views.View_Staff, name = 'viewstaff'),
    path('viewmember/', views.View_Member, name = 'viewmember'),
    path('contactvendor/', views.Contact_Vendor, name = 'contactvendor'),
    path('message/', views.Send_Message, name = 'message'),
    path('updatedata/', views.Update_Information, name = 'updatedata'),
    path('updatevendor/', views.Update_Vendor, name='updatevendor'),
    path('updatestaff/', views.Update_Staff, name='updatestaff'),
    path('updatemember/', views.Update_Member, name='updatemember'),
    path('loadupdatepassword/', views.Load_Update_Password, name='loadupdatepassword'),
    path('updatepassword/', views.Update_Password, name='updatepassword'),
    path('loadupdatestatus/', views.Load_Update_Status, name='loadupdatestatus'),
    path('updatestatus/', views.Update_Status, name='updatestatus'),
    path('subscription/', views.Subscriptions, name='subscription'),
    path('smssubscription/', views.SMSSubscriptions, name='smssubscription'),
    path('transaction/', views.Transactions, name='transaction'),
    path('transactiondetails/', views.TransactionDetails, name='transactiondetails'),
    path('rechargehistory/', views.RechargeHistory, name='rechargehistory'),
    path('smscreditrecharge/', views.SMSCreditRecharge, name='smscreditrecharge'),
    path('search/', views.Search, name='search'),
    path('loadcreatetable/', views.LoadCreateTable, name='loadcreatetable'),
    path('createtable/', views.GetCreateTable, name='createtable'),
    path('loadtablesdata/', views.Load_Tables_Data, name='loadtablesdata'),
    path('loadupdatetables/', views.Load_Update_Tables, name='loadupdatetables'),
    path('updatetables/', views.Update_Tables, name='updatetables'),
    path('deletetables/', views.Delete_Tables, name='deletetables'),
    path('booktables/', views.Book_Tables, name='booktables'),
    path('bookingdetails/<int:id>', views.Load_Booking_Details, name='bookingdetails'),
    path('booktable/', views.Confirm_BookTable, name='booktable'),
    path('viewmenu/', views.View_Menu, name='viewmenu'),
    path('loadorderdetails/', views.Load_Order_Details, name='loadorderdetails'),
    path('getorder/', views.Get_Order, name='getorder'),
    path('loadvariations/', views.Load_Variations, name='loadvariations'),

    path('vendorindex/', views.Load_Vendor_Index, name='vendorindex'),
    path('vendorstaff/', views.Load_Vendor_Staff, name='vendorstaff'),
    path('vendormember/', views.Load_Vendor_Member, name='vendormember'),
    path('vendorcontactform/', views.Vendor_ContacForm, name='vendorcontactform'),
    path('vendorupdateinformation/', views.Vendor_Update_Information, name='vendorupdateinformation'),
    path('vendorupdatestaff/', views.Vendor_Update_Staff, name='vendorupdatestaff'),
    path('vendorupdatemember/', views.Vendor_Update_Member, name='vendorupdatemember'),
    path('vendorloadupdatepassword/', views.Vendor_Load_Update_Password, name='vendorloadupdatepassword'),
    path('vendorupdatepassword/', views.Vendor_Update_Password, name='vendorupdatepassword'),
    path('vendorloadupdatestatus/', views.Vendor_Load_Update_Status, name='vendorloadupdatestatus'),
    path('vendorupdatestatus/', views.Vendor_Update_Status, name='vendorupdatestatus'),
    path('vendortransaction/', views.Vendor_Transactions, name='vendortransaction'),
    path('vendortransactiondetails/', views.Vendor_TransactionDetails, name='vendortransactiondetails'),
    path('vendorrechargehistory/', views.RechargeHistory, name='vendorrechargehistory'),

    path('loadvendorcreatediscount/', views.Load_CreateDiscount, name='loadvendorcreatediscount'),
    path('vendorcreatediscount/', views.CreateDiscount, name='vendorcreatediscount'),
    path('vendorviewdiscounts/', views.ViewDiscount, name='vendorviewdiscounts'),
    path('loadvendorupdatedeletediscount/', views.Load_DiscountUpdateDelete, name='loadvendorupdatedeletediscount'),
    path('vendorupdatediscount/', views.UpdateDiscount, name='vendorupdatediscount'),
    path('vendordeletediscount/', views.DeleteDiscount, name='vendordeletediscount'),

    # END JAWAD






    path('createpackages/', views.Create_Packages, name='createpackages'),
    path('createpackages/ajax', views.Create_Packages),
    path('viewpackages/editing', views.Package_Editing, name='editing'),
    path('viewpackages/', views.View_Packages, name='viewpackages'),
    path('viewpackages/editpackage', views.Edit_Packages, name='editpackages'),
    path('viewpackages/deletepackages', views.Delete_Packages, name='deletepackages'),
    # CREATE VENDOR MEMEBER STAFF URLS
    # path('signup',views.Signup,name='signup'),
    path('vendorsignup/', views.Vendor_Signup, name='vendorsignup'),
    path('membersignup/', views.Member_Signup, name='membersignup'),
    path('staffsignup/', views.staff_Signup, name='staffsignup'),
    path('createaccount/', views.CreateAccounts, name='createaccount'),
    path('validateemail/', views.Validations, name='validateemail'),

    # vendor Profile
    path('vendorprofile/', views.Vendor_Profile, name='vendorprofile'),
    # personal Profile settings passwrod
    path('personalprofile/', views.Personal_Profile, name='personalprofile'),
    path('profileSettings/', views.Settings_Profile, name='profileSettings'),
    path('validatepass/   ', views.PValidations, name='validatepass'),
    # personal Profile settings passwrod end
    # Super admin sign in urls
    path('login/', views.UserSignin, name='login'),
    path('login_authentication', views.UserSigninAuthenticattion, name='login_authentication'),
    path('logout/', views.logout, name='logout'),
#     CREATE GROUP URLS

    path('creategroup/', views.create_group, name='creategroup'),
    path('creategroup_action', views.creategroup_action, name='creategroup_action'),

    #admin vendor chat
    path('viewtutorial/', views.View_Tickets, name='viewtutorial'),
    path('addtutorial/', views.Add_Ticket, name='addtutorial'),
    path('viewtutorial/showconversation/<int:id>', views.Show_Conversation, name='showconversation'),
    path('reply/', views.Reply_Conversation, name='reply'),
    path('replytimer/', views.Reply_Timer, name='replytimer'),
    path('uploadfile/', views.Upload_Form, name='uploadfile'),
    path('unreadmessages/', views.Unread_Message, name='unreadmessages'),


#     MEssages URLS BRROAD CAST
    path('create_sms/', views.create_message_template, name='create_sms'),
    path('sendsms/', views.sendsms, name='sendsms'),
    path('create_email/', views.create_email_template, name='create_email'),
    path('create_event_sms/', views.create_event_message_template, name='create_event_sms'),
    path('create_event_email/', views.create_event_email_template, name='create_event_email'),


    path('createsmspackages/', views.Create_SMSPackages, name='createsmspackages'),
    path('viewsmspackages/', views.View_SMSPackages, name='viewsmspackages'),
    path('createsmspackages/smspackageCreationajax', views.Create_SMSPackages),
    path('viewsmspackages/', views.View_SMSPackages, name='viewsmspackages'),
    path('viewpackages/editsmspackage', views.Edit_SMSPackages, name='editsmspackages'),
    path('viewpackages/smsediting', views.Package_SMSEditing, name='smsediting'),
    path('viewpackages/deletesmspackages', views.Delete_SMSPackages, name='deletesmspackages'),


# Subcategories URL
    # create categories/subcategories urls
    path('createcategories/', views.Create_Categories, name='createcategories'),
    path('createcategories/CategoryCreation', views.Create_Categories),
    path('createsubcategories/', views.Create_SubCategories, name='createsubcategories'),
    path('createsubcategories/SubCategoryCreation', views.Create_SubCategories),
    path('viewcategories/', views.View_Categories, name='viewcategories'),
    path('viewcategories/editcategories', views.Edit_Categories, name='editcategories'),
    path('viewcategories/editingcategory', views.Editing_Category, name='editingcategory'),
    path('viewcategories/deletecategories', views.Delete_Categories, name='deletecategories'),
    path('viewsubcategories/', views.View_SubCategories, name='viewsubcategories'),
    path('viewsubcategories/editsubcategories', views.Edit_SubCategories, name='editsubcategories'),
    path('viewsubcategories/editingcategorysub', views.Editing_SubCategory, name='editingcategorysub'),
    path('viewsubcategories/deletesubcategories', views.Delete_SubCategories, name='deletesubcategories'),

#items Urls
    path('additems/', views.Add_Items, name='additems'),
    path('additems/additem', views.Add_Items),
    path('uploaditemimage/', views.Upload_ItemsImage, name='uploaditemimage'),
    path('viewitems/', views.View_Items, name='viewitems'),
    path('viewitems/deleteitems', views.Delete_Items, name='deleteitems'),
    path('viewitems/edititems', views.Edit_Items, name='edititems'),
    path('viewitems/editingitems', views.Editing_Items, name='editingitems'),

# tutorial url
    path('AddTutorials/', views.AddTutorial, name='AddTutorial'),
    path('EditTutorials/', views.EditTutorial, name='EditTutorial'),
    path('ShowCustomerTutorial/', views.ShowCustomerTutorial, name='ShowCustomerTutorial'),
    path('ShowVendorTutorial/', views.ShowVendorTutorial, name='ShowVendorTutorial'),
    path('ShowTutorialDetails/', views.ShowTutorialDetail, name='ShowTutorialDetail'),
    path('AddTutorialType/', views.AddTutorialType, name='AddTutorialType'),
    
#items Urls
    path('additems/', views.Add_Items, name='additems'),
    path('additems/additem', views.Add_Items),
    path('uploaditemimage/', views.Upload_ItemsImage, name='uploaditemimage'),
    path('viewitems/', views.View_Items, name='viewitems'),
    path('viewitems/deleteitems', views.Delete_Items, name='deleteitems'),
    path('viewitems/edititems', views.Edit_Items, name='edititems'),
    path('viewitems/editingitems', views.Editing_Items, name='editingitems'),
#item offers
    path('itemoffer/', views.Item_Offer, name='itemoffer'),
    path('creatingoffers', views.Creating_Offer, name='creatingoffers'),
    path('viewoffers', views.View_Offer, name='viewoffers'),
    path('viewitems/deleteoffer', views.Delete_Offers, name='deleteoffer'),
    path('viewitems/editoffers', views.Edit_Offers, name='editoffers'),
    path('viewitems/editingoffers', views.Editing_Offers, name='editingoffers'),



#  DB BACKUP URLS
    path('ShowBackup/', views.ShowBackup, name='Showdbbackup'),
    path('TakeBackup/', views.TakeBackup, name='Takedbbackup'),

    # Settings Work Start
    path('sms_setup/', views.SMS_Setup, name='sms_setup'),
    path('google_Setup/', views.google_Setup, name='google_Setup'),
    path('payment/', views.payment_Gateway, name='payment'),
    path('paypal/', views.paypal_Setup, name='paypal'),
    path('strip/', views.Strip_Setup, name='strip'),
    # setting work end


]