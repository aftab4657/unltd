from unltd.models import SMS_Setup,Google_Setup,Payment_Gateway

class Setups():

    request = ''
    def __init__(self,req):
        self.request = req

    def Sms_Setup(self):
        try:
            upid = self.request.POST.get('upid')
            act = self.request.POST.get('act')
            if(act == 'update'):
                apiservice = self.request.POST.get('apiservice')
                apikey = self.request.POST.get('apikey')
                cost = self.request.POST.get('cost')
                mrefil = self.request.POST.get('mrefil')
                recharge = self.request.POST.get('recharge')
                SMS_Setup.objects.filter(id=upid).update(servicename=apiservice, apikey=apikey, costtovendor=cost, refill=mrefil,
                              rechargealert=recharge, Status='inactive')

                return 'Saved'
            if (act == 'del'):
                try:
                    SMS_Setup.objects.filter(id=upid).delete()
                    return 'Deleted'
                except Exception as e:
                    print(e)
            if (act == 'activate'):
                try:
                    try:
                        SMS_Setup.objects.filter(Status='Active').update(Status='inactive')
                    except:
                        pass
                    SMS_Setup.objects.filter(id=upid).update(Status='Active')
                    return 'Activated'
                except:
                    return 'error'
            else:
                apiservice = self.request.POST.get('apiservice')
                apikey = self.request.POST.get('apikey')
                cost = self.request.POST.get('cost')
                mrefil = self.request.POST.get('mrefil')
                recharge = self.request.POST.get('recharge')
                c = SMS_Setup(servicename=apiservice, apikey=apikey, costtovendor=cost, refill=mrefil, rechargealert=recharge,Status='inactive')
                c.save()
                return 'Saved'
        except Exception as e:
            return e

    def Details_Sms(self):
        from django.db import connection
        cursor = connection.cursor()
        userid = self.request.session.get('id', "")
        cdata = []
        cursor.execute(
            "SELECT id,ServiceName,Api_Key,CostToVendor,MinimumRefill,RechargeAlert,Status from sms_setup")
        for row in cursor.fetchall():
            rdata = row
            cdata.append(row)
        return "Settings/SMS_Setup.html", cdata

    def Google_Setup(self):
        try:
            upid = self.request.POST.get('upid')
            act = self.request.POST.get('act')
            if(act == 'update'):
                mapapi = self.request.POST.get('mapapi')
                recaptchaapi = self.request.POST.get('recaptchaapi')
                analyticCode = self.request.POST.get('analyticCode')
                Google_Setup.objects.filter(id=upid).update(mapapi=mapapi, recaptchaapi=recaptchaapi, analyticCode=analyticCode)
                return 'Updated'
            if (act == 'del'):
                try:
                    Google_Setup.objects.filter(id=upid).delete()
                    return 'Deleted'
                except Exception as e:
                    print(e)
            else:
                mapapi = self.request.POST.get('mapapi')
                recaptchaapi = self.request.POST.get('recaptchaapi')
                analyticCode = self.request.POST.get('analyticCode')
                c = Google_Setup(mapapi=mapapi, recaptchaapi=recaptchaapi, analyticCode=analyticCode)
                c.save()
                return 'Saved'
        except Exception as e:
         return e

    def Details_Google(self):
        from django.db import connection
        cursor = connection.cursor()
        userid = self.request.session.get('id', "")
        cdata = []
        cursor.execute(
            "SELECT * from google_setup")
        for row in cursor.fetchall():
            rdata = row
            cdata.append(row)
        return "Settings/Google_Setup.html", cdata

    def payments_gateway(self):
        try:
            upid = self.request.POST.get('upid')
            act = self.request.POST.get('act')
            if(act=='update'):
                NameBank =  self.request.POST.get('bankname')
                NameAcc =  self.request.POST.get('accname')
                AccNo =  self.request.POST.get('accno')
                IbanNo =  self.request.POST.get('Ibanno')
                Payment_Gateway.objects.filter(id=upid).update(mailpaypal='', mailStripe='', NameBank=NameBank, NameAcc=NameAcc, AccNo=AccNo,
                                    IbanNo=IbanNo, CreditNo='', Type='Bank', Status='inactive')
                return 'Updated'
            if (act == 'activate'):
                try:
                    try:
                        Payment_Gateway.objects.filter(Status='Active', Type='Bank').update(Status='inactive')
                    except:
                        pass
                    Payment_Gateway.objects.filter(id=upid).update(Status='Active')
                    return 'Activated'
                except:
                    return 'error'
            else:
                NameBank = self.request.POST.get('NameBank')
                NameAcc = self.request.POST.get('NameAcc')
                AccNo = self.request.POST.get('AccNo')
                IbanNo = self.request.POST.get('IbanNo')
                c = Payment_Gateway(mailpaypal='', mailStripe='', NameBank=NameBank,NameAcc=NameAcc,AccNo=AccNo,IbanNo=IbanNo,CreditNo='',Type = 'Bank',Status='inactive')
                c.save()
                return 'Saved'
        except Exception as e:
         return e

    def Details_Bank(self):
        from django.db import connection
        cursor = connection.cursor()
        userid = self.request.session.get('id', "")
        cdata = []
        cursor.execute(
            "SELECT id,Bank_Name,Account_Name,Account_Number,IBAN_Number,Status from payment_gateway where type = 'Bank' ")
        for row in cursor.fetchall():
            rdata = row
            cdata.append(row)
        return "Settings/payment_Gateway.html", cdata

    #Paypal insert
    def paypal_Setup(self):
        try:
            mailpaypal = self.request.POST.get('mailpaypal')
            upid = self.request.POST.get('upid')
            act = self.request.POST.get('act')
            # if upid != 'No':
            if(act=='activate'):
                try:
                    try:
                        Payment_Gateway.objects.filter(Status='Active',Type='Paypal').update(Status='inactive')
                    except:
                        pass
                    Payment_Gateway.objects.filter(id=upid).update(Status='Active')
                    return 'Activated'
                except:
                    return 'error'
            if(act=='update'):
                try:
                    Payment_Gateway.objects.filter(id=upid).update(mailpaypal=mailpaypal)
                    return 'Updated'
                except:
                    return 'error'
            if(act == 'del'):
                try:
                    Payment_Gateway.objects.filter(id=upid).delete()
                    return 'Deleted'
                except Exception as e:
                    print (e)
            else:
                c = Payment_Gateway(mailpaypal=mailpaypal, mailStripe='', NameBank='',NameAcc='',AccNo='',IbanNo='',CreditNo='', Type='Paypal',Status='inactive')
                c.save()
                return 'Saved'
        except Exception as e:
         return e
    #paypal view
    def Details_Paypal(self):
        from django.db import connection
        cursor = connection.cursor()
        userid = self.request.session.get('id', "")
        cdata = []
        cursor.execute(
            "SELECT id,paypal_mail,status from payment_gateway where type = 'Paypal' ")
        for row in cursor.fetchall():
            rdata = row
            cdata.append(row)
        return "Settings/Paypal.html", cdata
    #Strip insert
    def strip_Setup(self):
        try:
            mailstrip = self.request.POST.get('mailstrip')
            upid = self.request.POST.get('upid')
            act = self.request.POST.get('act')
            # if upid != 'No':
            if(act=='activate'):
                try:
                    try:
                        Payment_Gateway.objects.filter(Status='Active',Type = 'strip').update(Status='inactive')
                    except:
                        pass
                    Payment_Gateway.objects.filter(id=upid).update(Status='Active')
                    return 'Activated'
                except:
                    return 'error'
            if(act=='update'):
                try:
                    Payment_Gateway.objects.filter(id=upid).update(mailStripe=mailstrip)
                    return 'Updated'
                except:
                    return 'error'
            if(act == 'del'):
                try:
                    Payment_Gateway.objects.filter(id=upid).delete()
                    return 'Deleted'
                except Exception as e:
                    print (e)
            else:
                c = Payment_Gateway(mailpaypal='', mailStripe=mailstrip, NameBank='',NameAcc='',AccNo='',IbanNo='',CreditNo='', Type='strip',Status='inactive')
                c.save()
                return 'Saved'
        except Exception as e:
         return e
    #Strip view
    def Details_strip(self):
        from django.db import connection
        cursor = connection.cursor()
        userid = self.request.session.get('id', "")
        cdata = []
        cursor.execute(
            "SELECT id,Strip_mail,status from payment_gateway where type = 'Strip' ")
        for row in cursor.fetchall():
            rdata = row
            cdata.append(row)
        return "Settings/Strip.html", cdata