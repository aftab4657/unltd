import os
from datetime import datetime
import qrcode
from django.utils import timezone
from UNLTDjango.settings import BASE_DIR
from unltd.models import Location,User,Vendor,Member,Staff
import smtplib,string,random
from random import randint

class Registration():

    request = ''

    def __init__(self,req):
        self.request = req

    def Vendor_Signup(self):
        try:
            dname = self.request.POST.get('dname')
            bname = self.request.POST.get('bname')
            email = self.request.POST.get('email')
            bemail = self.request.POST.get('bemail')
            country = self.request.POST.get('country')
            try:
            #Country abbrivation
             spc=country.split(',')
             gl = spc[-1]
             year = datetime.today().year
             vuid = 'V'+str(gl)+str(year).replace('20','')
            except Exception as Idexception:
                print(Idexception)
            state = self.request.POST.get('state')
            city = self.request.POST.get('city')
            postal = self.request.POST.get('postal')
            address = self.request.POST.get('address')
            baddress = self.request.POST.get('baddress')
            phone = self.request.POST.get('phone')
            bphone = self.request.POST.get('bphone')
            industry = self.request.POST.get('industry')
            sname = self.request.POST.get('sname')
            uname = self.request.POST.get('user')
            passw = self.request.POST.get('password')
            sm = MailSend(email)
            vcode = sm.Sendmailer()
            if vcode != 'Error while Sending mail':
                s = User(userid=vuid, displayname=dname, email=email, mobile=phone, password=passw,
                         image='No Image',
                         registerdate=datetime.now(tz=timezone.utc), lastupdateddate=datetime.now(tz=timezone.utc), status='Not Verified',
                         forgotpassword=vcode,
                         usertype=uname,)
                try:
                 s.save()
                except Exception as t1:
                 return t1
                try:
                    uid = User.objects.latest('id')
                    s = str(uid).split()
                    s1=s[-1]
                    iddigit = s1.replace('(','').replace(')','')
                    tdgit = len(iddigit)
                    finalid =''
                    for x in range(7-tdgit):
                        finalid += '0'
                    vuid = vuid+finalid+iddigit+random.choice(string.ascii_letters)
                    User.objects.filter(id=s1.replace('(','').replace(')','')).update(userid=vuid)
                except Exception as lastid:
                    return lastid
                c = Location(userid=uid,address=address,city=city,postcode=postal,state=state,country=country)
                c.save()
                b = Vendor(userid=uid, businessname=bname, businessemail=bemail, businesscontact=bphone, industry=industry, systemname=sname,businessaddress=baddress)
                b.save()
                return 'Saved'
           # return vcode
        except Exception as t3:
            return t3

    def Staff_Signup(self):
        try:
            dname = self.request.POST.get('dname')
            email = self.request.POST.get('email')
            country = self.request.POST.get('country')
            try:
                # Country abbrivation
                spc = country.split(',')
                gl = spc[-1]
                year = datetime.today().year
                vuid = 'M' + str(gl) + str(year).replace('20', '')
            except Exception as Idexception:
                print(Idexception)
            state = self.request.POST.get('state')
            city = self.request.POST.get('city')
            postal = self.request.POST.get('postal')
            address = self.request.POST.get('address')
            phone = self.request.POST.get('phone')
            uname = self.request.POST.get('user')
            passw = self.request.POST.get('password')
            privilege = self.request.POST.get('privilege')
            department = self.request.POST.get('department')

            sm = MailSend(email)
            vcode = sm.Sendmailer()
            if vcode != 'Error while Sending mail':
                s = User(userid=vuid, displayname=dname, email=email, mobile=phone, password=passw,
                         image='No Image',
                         registerdate=datetime.now(tz=timezone.utc), lastupdateddate=datetime.now(tz=timezone.utc),
                         status='Not Verified',
                         forgotpassword=vcode,
                         usertype=uname, )
                try:
                    s.save()
                except Exception as t1:
                    return t1
                try:
                    uid = User.objects.latest('id')
                    s = str(uid).split()
                    s1 = s[-1]
                    iddigit = s1.replace('(', '').replace(')', '')
                    tdgit = len(iddigit)
                    finalid = ''
                    for x in range(7 - tdgit):
                        finalid += '0'
                    vuid = vuid + finalid + iddigit + random.choice(string.ascii_letters)
                    User.objects.filter(id=s1.replace('(', '').replace(')', '')).update(userid=vuid)
                except Exception as lastid:
                    print(lastid)
                c = Location(userid=uid, address=address, city=city, postcode=postal, state=state, country=country)
                c.save()
                try:
                    b = Staff(userid=uid, privilege=privilege, department=department)
                    b.save()
                except Exception as e:
                    print(e)
                return 'Saved'
            # return vcode
        except Exception as t3:
            return t3

    def Member_Signup(self):
        try:
            dname = self.request.POST.get('dname')
            email = self.request.POST.get('email')
            country = self.request.POST.get('country')
            try:
                # Country abbrivation
                spc = country.split(',')
                gl = spc[-1]
                year = datetime.today().year
                vuid = 'M' + str(gl) + str(year).replace('20', '')
            except Exception as Idexception:
                print(Idexception)
            state = self.request.POST.get('state')
            city = self.request.POST.get('city')
            postal = self.request.POST.get('postal')
            address = self.request.POST.get('address')
            phone = self.request.POST.get('phone')
            uname = self.request.POST.get('user')
            passw = self.request.POST.get('password')
            dob = self.request.POST.get('rdate')
            gender = self.request.POST.get('gender')
            sm = MailSend(email)
            vcode = sm.Sendmailer()
            if vcode != 'Error while Sending mail':
                s = User(userid=vuid, displayname=dname, email=email, mobile=phone, password=passw,
                         image='No Image',
                         registerdate=datetime.now(tz=timezone.utc), lastupdateddate=datetime.now(tz=timezone.utc),
                         status='Not Verified',
                         forgotpassword=vcode,
                         usertype=uname, )
                try:
                    s.save()
                except Exception as t1:
                    return t1
                try:
                    uid = User.objects.latest('id')
                    s = str(uid).split()
                    s1 = s[-1]
                    iddigit = s1.replace('(', '').replace(')', '')
                    tdgit = len(iddigit)
                    finalid = ''
                    for x in range(7 - tdgit):
                        finalid += '0'
                    vuid = vuid + finalid + iddigit + random.choice(string.ascii_letters)
                    User.objects.filter(id=s1.replace('(', '').replace(')', '')).update(userid=vuid)
                except Exception as lastid:
                    print(lastid)
                c = Location(userid=uid, address=address, city=city, postcode=postal, state=state, country=country)
                c.save()
                try:
                    bdata = {
                        'UserId': vuid,
                        'Name': dname,
                        'Email': email,
                        'Phone': phone,
                        'City': city,
                        'Country': country,
                        'DOB': dob,
                        'Gender': gender,
                    }
                    q = QRCode(bdata)
                    mq = q.Create_QR_Code()
                    b = Member(userid=uid, dateofbirth=dob,qrcode=mq ,gender=gender)
                    b.save()

                except Exception as e:
                    return e
                return 'Saved'
            # return vcode
        except Exception as t3:
            return t3

class MailSend():
    mail =''
    def __init__(self,email):
        self.mail = email
    def Sendmailer(self):
        gmail_user = 'softwarepatterns005@gmail.com'
        gmail_password = 's00998877'
        sent_from = gmail_user
        to = [self.mail]
        subject = 'Vrification Code'
        rnumber = randint(10000, 99999)
        body = 'Your Authorization Code is = ' + str(rnumber)
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
            return str(rnumber)
        except:
           print('Error while Sending mail')

class QRCode():
    data =''
    def __init__(self,data):
        self.data = data
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
        qrcodename = 'QR'+(self.data['UserId'])
        qrcodepath = os.path.join(BASE_DIR,'unltd/static/QR_Codes/')
        img.save(qrcodepath+qrcodename+"image.jpg")
        return qrcodename+"image.jpg"
