from django.db import models

# Create your models here.
class Api(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    apiaccesskey = models.CharField(db_column='ApiAccessKey', max_length=50)  # Field name made lowercase.
    apisecretkey = models.CharField(db_column='ApiSecretKey', max_length=50)  # Field name made lowercase.
    apiname = models.CharField(db_column='ApiName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'api'


class Booking(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    tableid = models.ForeignKey('Tables', models.CASCADE, db_column='TableId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'booking'


class Category(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=50)  # Field name made lowercase.
    timerange = models.DateTimeField(db_column='TimeRange')  # Field name made lowercase.
    creationddate = models.DateTimeField(db_column='CreatedDate', auto_now=True)

    class Meta:
        managed = True
        db_table = 'category'

class Developersuse(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    tag = models.TextField(db_column='Tag')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'developersuse'


class Images(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.CASCADE, db_column='ItemId')  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'images'


class Item(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    subcategoryid = models.ForeignKey('Subcategory', models.CASCADE, db_column='SubCategoryId')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName',max_length=225)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=225)  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible')  # Field name made lowercase.
    itemdisplayid = models.ForeignKey('Itemdisplay', models.CASCADE, db_column='ItemDisplayId')  # Field name made lowercase.
    preparetime = models.IntegerField(db_column='PrepareTime',default=45)  # Field name made lowercase.
    itemimage = models.CharField(db_column='ItemImage', max_length=225, default=None)
    creationddate = models.DateTimeField(db_column='CreatedDate',auto_now=True)

    class Meta:
        managed = True
        db_table = 'item'


class Itemdisplay(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    displaytype = models.CharField(db_column='DisplayType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'itemdisplay'


class Itemorder(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    oderid = models.ForeignKey('Orders', models.CASCADE, db_column='OderId')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=225)  # Field name made lowercase.
    itemvariation = models.CharField(db_column='VariationName', max_length=225, default=None)  # Field name made lowercase.
    itemprice = models.IntegerField(db_column='ItemPrice', default=None)  # Field name made lowercase.
    itemquantity = models.IntegerField(db_column='ItemQuantity', default=None)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', default=None)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate',auto_now=True)

    class Meta:
        managed = True
        db_table = 'itemorder'

class Languages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    languagename = models.CharField(db_column='LanguageName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'languages'


class Location(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=225)  # Field name made lowercase.
    city = models.CharField(max_length=20)
    postcode = models.IntegerField(db_column='PostCode', default=0000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state = models.CharField(db_column='State', max_length=20)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'location'


class Member(models.Model):
    sr_no = models.AutoField(db_column='Sr_No', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10)  # Field name made lowercase.
    qrcode = models.TextField(db_column='QRCode')  # Field name made lowercase.
    vendor = models.ForeignKey('VendorStaff', models.CASCADE, db_column='VendorId', default=1)

    class Meta:
        managed = True
        db_table = 'member'

class Membership(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    packageid = models.ForeignKey('Subscription', models.CASCADE, db_column='PackageId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'membership'


class Menu(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    menuid = models.IntegerField(db_column='MenuId', default=None)
    name = models.CharField(db_column='Name', max_length=225, default=None)  # Field name made lowercase
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.CASCADE, db_column='ItemId')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'menu'


class Messages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    senderid = models.ForeignKey('Messagesender', models.CASCADE, db_column='SenderId')  # Field name made lowercase.
    receiverid = models.ForeignKey('User', models.CASCADE, db_column='ReceiverId')  # Field name made lowercase.
    messagehead = models.CharField(db_column='MessageHead', max_length=225)  # Field name made lowercase.
    messagebody = models.CharField(db_column='MessageBody', max_length=225)  # Field name made lowercase.
    eventdate = models.DateTimeField(db_column='EventDate', auto_now_add=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'messages'


class Messagesender(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'messagesender'


class Orders(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vendorid = models.ForeignKey('Venderorders', models.CASCADE, db_column='VendorId')  # Field name made lowercase.
    memberid = models.ForeignKey('User', models.CASCADE, db_column='MemberId')  # Field name made lowercase.
    totalamount = models.IntegerField(db_column='TotalAmount',default=None)  # Field name made lowercase.
    ordertype = models.CharField(db_column='OrderType', max_length=50, default=None)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=50)  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TotalTime',default=None)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DiscountAmount', default=None)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'orders'


class Packages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    packagename = models.CharField(db_column='PackageName', max_length=225)  # Field name made lowercase.
    packagedetail = models.CharField(db_column='PackageDetail', max_length=225)  # Field name made lowercase.
    packagecharges = models.IntegerField(db_column='PackageCharges',default=None)  # Field name made lowercase.
    packageduration = models.IntegerField(db_column='PackageDuration',default=None)  # Field name made lowercase.
    packagetype = models.CharField(db_column='PackageType',max_length=225, default= None)
    packagecreationdate = models.DateTimeField(db_column='CreatedDate',auto_now=True)

    class Meta:
        managed = True
        db_table = 'packages'


class Itemofferoptions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.CASCADE, db_column='ItemId')  # Field name made lowercase.
    customoffer = models.CharField(db_column='CustomOffer', max_length=225)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price',default=None)  # Field name made lowercase.
    timerange = models.DateTimeField(db_column='TimeRange')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'itemofferoptions'

class Staff(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    privilege = models.CharField(db_column='Privilege', max_length=20)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=20)  # Field name made lowercase.
    vendor = models.ForeignKey('VendorStaff',models.CASCADE,db_column='VendorId',default=1)

    class Meta:
        managed = True
        db_table = 'staff'

class Subcategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.CASCADE, db_column='CategoryId')  # Field name made lowercase.
    subcategoryname = models.CharField(db_column='SubCategoryName', max_length=50)  # Field name made lowercase.
    timerange = models.DateTimeField(db_column='TimeRange')  # Field name made lowercase.
    creationddate = models.DateTimeField(db_column='CreatedDate', auto_now=True)

    class Meta:
        managed = True
        db_table = 'subcategory'


class Subscription(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    packageid = models.ForeignKey(Packages, models.CASCADE, db_column='PackageId')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId', default=None)
    subscriptiondate = models.DateTimeField(db_column='SubscriptionDate',auto_now=True)
    expirydate = models.DateTimeField(db_column='ExpiryDate',auto_now=True)
    autorenew = models.IntegerField(db_column='AutoRenew')  # Field name made lowercase.
    freetrail = models.IntegerField(db_column='FreeTrail')  # Field name made lowercase.
    expiryalert = models.IntegerField(db_column='ExpiryAlert')  # Field name made lowercase.
    renewconfirmation = models.IntegerField(db_column='RenewConfirmation')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'subscription'

class SMSSubscription(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    packageid = models.ForeignKey('SMSPackages', models.CASCADE, db_column='PackageId')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId', default=None)
    subscriptiondate = models.DateTimeField(db_column='SubscriptionDate',auto_now=True)
    expirydate = models.DateTimeField(db_column='ExpiryDate',auto_now=True)
    autorenew = models.IntegerField(db_column='AutoRenew')  # Field name made lowercase.
    freetrail = models.IntegerField(db_column='FreeTrail')  # Field name made lowercase.
    expiryalert = models.IntegerField(db_column='ExpiryAlert')  # Field name made lowercase.
    renewconfirmation = models.IntegerField(db_column='RenewConfirmation')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'smssubscription'


class Superadmin(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'superadmin'


class Tables(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId')  # Field name made lowercase.
    tabletype = models.CharField(db_column='TableType', max_length=50)  # Field name made lowercase.
    tabledescription = models.CharField(db_column='TableDescription', max_length=225, default=None)  # Field name made lowercase.
    tablecapacity = models.IntegerField(db_column='TableCapacity')  # Field name made lowercase.
    availible = models.CharField(db_column='Availible', max_length=50)  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCode', max_length=225, default=None)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tables'


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=225)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=225)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=225)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=50)  # Field name made lowercase.
    registerdate = models.DateTimeField(db_column='RegisterDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    forgotpassword = models.CharField(db_column='ForgotPassword', max_length=10)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=50)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance',default=None)
    expirydate = models.DateTimeField(db_column='ExpiryDate')

    class Meta:
        managed = True
        db_table = 'user'


class Venderorders(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.CASCADE, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'venderorders'


class Vendor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.CASCADE, db_column='UserId')  # Field name made lowercase.
    businessname = models.CharField(db_column='BusinessName', max_length=50)  # Field name made lowercase.
    businessemail = models.CharField(db_column='BusinessEmail', max_length=225)  # Field name made lowercase.
    businesscontact = models.CharField(db_column='BusinessContact', max_length=225)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=225)  # Field name made lowercase.
    systemname = models.CharField(db_column='SystemName', max_length=225)  # Field name made lowercase.
    businessaddress = models.TextField(db_column='BusinessAddress')  # Field name made lowercase.
    businesslogo = models.TextField(db_column='BusinessLogo')  # Field name made lowercase.
    businessicon = models.TextField(db_column='BusinessIcon')  # Field name made lowercase.
    heroicon = models.TextField(db_column='HeroIcon')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'vendor'

class Transaction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    mode = models.CharField(db_column='Mode',max_length=225,default=None)
    amount = models.IntegerField(db_column='Amount',default=None)
    date = models.DateTimeField(db_column='Date',auto_now_add=True)
    orderid = models.ForeignKey(Orders,models.CASCADE,default=None,db_column='OrderId')
    memberid = models.IntegerField(db_column='Member')
    waiterid = models.IntegerField(db_column='Waiter', default=None)
    cashierid = models.IntegerField(db_column='Cashier', default=None)
    discount = models.CharField(db_column='Discount',max_length=225, default='No Discount')

    class Meta:
        managed = True
        db_table = 'transaction'

class RechargeHistory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.CASCADE, db_column='UserId')  # Field name made lowercase.
    date = models.DateTimeField(db_column='EventDate',auto_now_add=True)
    type = models.CharField(db_column='RechargeType',max_length=225)
    amount = models.IntegerField(db_column='Amount',default=None)
    purpose = models.CharField(db_column='RechergePurpose',max_length=225,default=None)

    class Meta:
        managed = True
        db_table = 'rechargehistory'

class QAReplies(models.Model):
    reply_id=models.AutoField(db_column='ReplyId', primary_key=True)
    #question_id=models.ForeignKey('QASupport', models.CASCADE, db_column='QuestionId')
    question_id=models.IntegerField( db_column='QuestionId')
    reply_text= models.CharField(db_column='ReplyText', max_length=250)
    reply_file=models.CharField(db_column='ReplyFile', max_length=150)
    reply_by=models.CharField(db_column='ReplyBy', max_length=150)
    user_id=models.ForeignKey(User,models.CASCADE,db_column='Userid',default=None)
    reply_date=models.DateTimeField(db_column='ReplyDate')
    read_reply=models.IntegerField( db_column='ReadReply')
    class Meta:
        managed = True
        db_table = 'QAReplies'


class QASupport(models.Model):
    question_id= models.AutoField(db_column='QuestionId', primary_key=True)
    question_title=models.CharField(db_column='QuestionTitle', max_length=150)
    question_text=models.CharField(db_column='QuestionText', max_length=250)
    question_file=models.CharField(db_column='QuestionFile', max_length=250)
    question_by=models.CharField(db_column='QuestionBy', max_length=150)
    priority=models.CharField(db_column='Priority', max_length=50)
    status=models.CharField(db_column='Status', max_length=50)
    question_date=models.DateTimeField(db_column='QuestionDate')
    read_question=models.IntegerField( db_column='ReadQuestion')
    user_id=models.ForeignKey(User,models.CASCADE,db_column='Userid',default=None)

    class Meta:
        managed = True
        db_table = 'QASupports'


class SMSPackages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    smspackagename = models.CharField(db_column='SMSPackageName', max_length=225)  # Field name made lowercase.
    smspackagedetail = models.CharField(db_column='SMSPackageDetail', max_length=225)  # Field name made lowercase.
    smspackagecharges = models.IntegerField(db_column='PackageCharges',default=None)  # Field name made lowercase.
    smspackageduration = models.CharField(db_column='SMSPackageDuration', max_length=225)  # Field name made lowercase.
    smspackagetype = models.CharField(db_column='SMSPackageType', max_length=225, default=None)
    totalsms = models.IntegerField(db_column='TotalSMS', default=None)
    packagecreationdate = models.DateTimeField(db_column='CreatedDate', auto_now=True)

    class Meta:
        managed = True
        db_table = 'SMSPackages'

class Currency(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=225)

    class Meta:
        managed = True
        db_table = 'Currency'

class GeneralSetting(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=225)
    currency = models.CharField(db_column='Currency', max_length=225)
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserId',default=None)

    class Meta:
        managed = True
        db_table = 'GeneralSetting'

class Group(models.Model):
    group_id = models.AutoField(db_column='GroupId',primary_key=True)
    title = models.CharField(db_column='Title', max_length=255)
    description = models.TextField(db_column='Description')
    userid = models.ForeignKey(User, models.CASCADE, db_column='UserId')
    class Meta:
        managed = True
        db_table = 'Group'

class GroupMember(models.Model):
    memberid = models.AutoField(db_column='MemberId',primary_key=True)
    group_id = models.ForeignKey(Group, models.CASCADE, db_column='GroupId')
    userid = models.ForeignKey(User, models.CASCADE, db_column='UserId', default=None, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=225)
    class Meta:
        managed = True
        db_table = 'GroupMember'


class BroadCastEventMessages(models.Model):
    msgid = models.AutoField(db_column='MessageId',primary_key=True)
    title = models.CharField(db_column='Title', max_length=255)
    description = models.TextField(db_column='Description')
    senderid = models.ForeignKey(User, models.CASCADE, db_column='SenderId')
    type = models.CharField(db_column='Type', max_length=255)    #This is type to check that message is SMS or Email
    msgtype = models.CharField(db_column='MessageType', max_length=255)    #This is type to check that message is broad cast message or event
    status = models.CharField(db_column='Status', max_length=255)
    class Meta:
        managed = True
        db_table = 'BroadCastEventMessages'

class ItemVariation(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)
    itemid= models.ForeignKey(Item,models.CASCADE,db_column="ItemId")
    title = models.CharField(db_column='Title', max_length=255)
    description = models.CharField(db_column='Description', max_length=255)
    discount = models.IntegerField(db_column='Discount', default=None)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', default=None)

    class Meta:
        managed = True
        db_table = 'ItemVariation'


class Tutorial(models.Model):
    id = models.AutoField(db_column='tutorial_id', primary_key=True)  # Field name made lowercase.
    long_text = models.TextField(db_column='long_text')  # Field name made lowercase.
    feature_image=models.TextField(db_column='feature_image',max_length=255)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='created_date')  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='modified_date')  # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=255)  # Field name made lowercase.
    group=models.CharField(db_column='group',max_length=30,default=None)
    type=models.ForeignKey('TutorialType',models.DO_NOTHING,db_column='type',related_name='tutorialtype')
    class Meta:
        managed = True
        db_table = 'tutorial'

class TutorialType(models.Model):
    id=models.AutoField(db_column='id', primary_key=True)
    name=models.CharField(db_column='name',max_length=255,default=None)
    class Meta:
        managed = True
        db_table = 'tutorialtype'
class Backup(models.Model):
    id = models.AutoField(db_column='db_id', primary_key=True)  # Field name made lowercase.
    filename = models.CharField(db_column='filename',max_length=255)  # Field name made lowercase.
    filesize=models.CharField(db_column='size',max_length=255)
    process=models.CharField(db_column='process',max_length=20,default=None)
    created_date = models.DateTimeField(db_column='created_date')  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'backup'

class VendorStaff(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)
    userid = models.ForeignKey(User,models.CASCADE,db_column='UserId')

    class Meta:
        managed = True
        db_table = 'VendorStaff'


class VendorMember(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)
    userid = models.ForeignKey(User,models.CASCADE,db_column='UserId')
    class Meta:
        managed = True
        db_table = 'VendorMember'


class VendorDiscount(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)
    userid = models.ForeignKey(User,models.CASCADE,db_column='UserId')
    title = models.CharField(db_column='Title',max_length=225,default=None)
    discount = models.IntegerField(db_column='Discount')
    createdat= models.DateTimeField(db_column='CreatedDate',auto_now=True)
    expirydate = models.DateTimeField(db_column='ExpiryDate')
    type = models.CharField(db_column='Type',max_length=225,default='FixedAmount')
    class Meta:
        managed = True
        db_table = 'VendorDiscount'

class Itemofferoption(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.CASCADE, db_column='ItemId')  # Field name made lowercase.
    customoffer = models.CharField(db_column='CustomOffer', max_length=225)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price',default=None)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartTimeRange',default=None)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndTimeRange',default=None)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreatedDate',auto_now=True)
    class Meta:
        managed = True
        db_table = 'itemofferoption'

class SMS_Setup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', max_length=225)
    apikey = models.CharField(db_column='Api_key', max_length=225)
    costtovendor = models.IntegerField(db_column='CostToVendor', default = None)
    refill = models.IntegerField(db_column='MinimumRefill', default=None)
    rechargealert = models.IntegerField(db_column='RechargeAlert', default=None)
    Status = models.CharField(db_column='Status', max_length=225,default=None)
    class Meta:
        managed = True
        db_table = 'SMS_Setup'

class Google_Setup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    mapapi = models.CharField(db_column='Map_API', max_length=225)
    recaptchaapi = models.CharField(db_column='ReCaptcha_API', max_length=225)
    analyticCode = models.CharField(db_column='Analytic_Code', max_length=225)
    class Meta:
        managed = True
        db_table = 'Google_Setup'

class Payment_Gateway(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    mailpaypal = models.CharField(db_column='Paypal_Mail', max_length=225,default=None)
    mailStripe = models.CharField(db_column='Strip_Mail', max_length=225,default=None)
    NameBank = models.CharField(db_column='Bank_Name', max_length=225,default=None)
    NameAcc = models.CharField(db_column='Account_Name', max_length=225,default=None)
    AccNo =  models.CharField(db_column='Account_Number', max_length=225,default=None)
    IbanNo = models.CharField(db_column='IBAN_Number', max_length=225,default=None)
    CreditNo = models.CharField(db_column='Credit_Card_No', max_length=225,default=None)
    Type = models.CharField(db_column='Type', max_length=225,default=None)
    Status = models.CharField(db_column='Status', max_length=225,default=None)
    class Meta:
        managed = True
        db_table = 'Payment_Gateway'



