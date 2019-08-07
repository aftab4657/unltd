from unittest.test.testmock.testpatch import Foo
from django.utils import timezone
from requests import request

from ..models import Packages, Location, QASupport, QAReplies, User
from django.core.files.storage import FileSystemStorage
import smtplib
from random import randint
from datetime import datetime
from django.core import serializers
from django.db.models import Q
from ..items.item import AddItems


class AddTickets():
    request=''
    def __init__(self,req):
        self.request=req
    def Add_Tickets(self):
        try:
            title = (self.request.POST.get('Title'))
            priority = (self.request.POST.get('priority'))
            description = (self.request.POST.get('Description'))
            userid=User.objects.filter(id=self.request.session['id'])[0]
            obj=AddItems(request)
            idchange=obj.id_generator()

            if self.request.POST.get('file') != '':
                file = self.request.FILES['file']
                fs = FileSystemStorage()
                filename = (idchange + "_" + file.name).replace(" ", "")
                fs.save(filename, file)
            else:
                filename=''

            p=QASupport(question_title=title,question_text=description,question_file=filename,question_by=self.request.session['DisplayName'],userid=userid,priority=priority,status='open',question_date=datetime.now(),read_question=0)
            p.save()
            msg =True
            return (msg)
        except Exception as e:
            return False

class ViewTickets():
    request = ''

    def __init__(self, req):
        self.request = req

    def View_Tickets(self):
        data = []
        if self.request.session['UserType'].lower() == "SuperAdmin".lower():
            tickets = QASupport.objects.all()
            for ticket in tickets:
                data.append(
                    [ticket.question_id,ticket.question_title,ticket.question_text,ticket.question_file,ticket.userid.displayname,ticket.userid.id,ticket.priority,ticket.status,ticket.question_date])
        else:
            tickets = QASupport.objects.filter(userid=self.request.session['id'])
            for ticket in tickets:
                data.append(
                    [ticket.question_id, ticket.question_title, ticket.question_text, ticket.question_file,
                     ticket.userid.displayname, ticket.userid.id, ticket.priority, ticket.status, ticket.question_date])

        context = {
            "Data": data
        }
        return context

class ShowMessages():
    request = ''
    def __init__(self, req,tid):
        self.request = req
        self.ticketid = tid

    def Show_Messages(self):
        data = []
        datareply=[]
        lastid=''
        readed = QASupport.objects.filter(question_id=self.ticketid).update(read_question=1)
        question = QASupport.objects.filter(question_id=self.ticketid)
        for message in question:
            data.append([message.question_title,message.question_text,message.question_file,message.userid.displayname,message.userid.id,message.question_date,self.ticketid])
        reply = QAReplies.objects.filter(question_id=self.ticketid).order_by('-reply_id')

        for msg in reply:
            datareply.append([msg.reply_id,msg.question_id,msg.reply_text,msg.reply_file,msg.userid.displayname,msg.userid.id,msg.reply_date])
            lastid=msg.reply_id
        context = {
            "Data": data,
            "Replies":datareply,
            "LastID":lastid
        }
        return context

class AddReply():
    request = ''
    def __init__(self, req):
        self.request = req
    def Add_Reply(self):
        try:
            closeticket = (self.request.POST.get('Cticket'))
            q_id = (self.request.POST.get('Qid'))
            replytext = (self.request.POST.get('reply'))
            replyby = self.request.session['DisplayName']
            userid = User.objects.filter(id=self.request.session['id'])[0]
            replydate = datetime.now()
            if (closeticket == 'close'):
                r = QAReplies(question_id=q_id, reply_text=replytext, reply_by=replyby, userid=userid,
                              reply_date=replydate, reply_file='',read_reply=0)
                r.save()
                c = QASupport.objects.filter(question_id=q_id).update(status=closeticket)
                return 'close'
            else:

                r = QAReplies(question_id=q_id, reply_text=replytext, reply_by=replyby, userid=userid,
                              reply_date=replydate, reply_file='',read_reply=0)

                r.save()
                uid = QAReplies.objects.latest('reply_id')
                s = str(uid).split()
                s1 = s[-1]
                iddigit = s1.replace('(', '').replace(')', '')
                return iddigit


        except Exception as e:
            return False

class ShowUpdatedMessages():
    request = ''

    def __init__(self, req,qid,lid):
        self.request = req
        self.qid = qid
        self.lid = lid

    def Show_UpdatedMessages(self):
        data = []
        datareply=[]
        print("ques id ====", self.qid)
        print("last id ====",self.lid)
        question = QASupport.objects.filter(question_id=self.qid)
        for message in question:
            data.append([message.question_title,message.question_text,message.question_file,message.userid.displayname,message.userid.id,message.question_date,self.qid])
        reply = QAReplies.objects.filter(question_id=self.qid ).filter(reply_id__gt=int(self.lid))
        for msg in reply:
            timestampStr=msg.reply_date.strftime("%B %d, %Y, %#I:%M %p.")
            timestampStr = timestampStr[:-3] + timestampStr[-3:-2].lower() + '.' + timestampStr[-2:-1].lower()
            datareply.append([msg.reply_id,msg.question_id,msg.userid.displayname,msg.reply_file,msg.reply_by,msg.userid.id,timestampStr,msg.reply_text])
            #length of datareply will be equal to unread msgs [if length >0 then read_reply=1]
        if (len(datareply)>0):
            readed = QAReplies.objects.filter(question_id=self.qid).update(read_reply=1)
        context = {
            "Data": data,
            "Replies":datareply
        }
        return context
class UploadFile():
    request=''
    def __init__(self,req):
        self.request=req
    def Upload_File(self):
        try:
            replytext = (self.request.POST.get('reply'))
            closeticket = (self.request.POST.get('Cticket'))
            q_id = (self.request.POST.get('Qid'))
            if self.request.POST.get('file') != '':
                file = self.request.FILES['file']
                fs = FileSystemStorage()
                filename = (idchange + "_" + file.name).replace(" ", "")
                fs.save(filename, file)
            else:
                filename=''
            data = []
            datareply = []
            replyby = self.request.session['DisplayName']
            userid = User.objects.filter(id=self.request.session['id'])[0]
            replydate = datetime.now()
            if(replytext!=''):

                if (closeticket == 'close'):
                    r = QAReplies(question_id=q_id, reply_text=replytext, reply_by=replyby, userid=userid,
                                  reply_date=replydate, reply_file=filename,read_reply=0)
                    r.save()
                    c = QASupport.objects.filter(question_id=q_id).update(status=closeticket)
                    return 'close'
                else:

                    r = QAReplies(question_id=q_id, reply_text=replytext, reply_by=replyby, userid=userid,
                                  reply_date=replydate, reply_file=filename,read_reply=0)

                    r.save()
                    question = QASupport.objects.filter(question_id=q_id)
                    for message in question:
                        data.append(
                            [message.question_title, message.question_text, message.question_file, message.userid.displayname,
                             message.userid.id, message.question_date, q_id])
                    reply = QAReplies.objects.filter(question_id=q_id).order_by('-reply_id')

                    for msg in reply:
                        datareply.append(
                            [msg.reply_id, msg.question_id, msg.reply_text, msg.reply_file, msg.userid.displayname, msg.userid.id,
                             msg.reply_date])
                        lastid = msg.reply_id
                    context = {
                        "Data": data,
                        "Replies": datareply,
                        "LastID": lastid
                    }
                    return 'TRUE',context
                    #return iddigit
            else:
                question = QASupport.objects.filter(question_id=q_id)
                for message in question:
                    data.append(
                        [message.question_title, message.question_text, message.question_file, message.userid.displayname,
                         message.userid.id, message.question_date, q_id])
                reply = QAReplies.objects.filter(question_id=q_id).order_by('-reply_id')

                for msg in reply:
                    datareply.append(
                        [msg.reply_id, msg.question_id, msg.reply_text, msg.reply_file, msg.userid.displayname, msg.userid.id,
                         msg.reply_date])
                    lastid = msg.reply_id
                context = {
                    "Data": data,
                    "Replies": datareply,
                    "LastID": lastid
                }
                return 'ERROR',context


        except Exception as e:
            return False




class ShowUnreadMessages():
    request = ''
    def __init__(self, req):
        self.request = req

    def Show_Unread_Messages(self):
        lastmsgs = []
        lastQues=[]
        data1=[]
        uid = User.objects.filter(id=self.request.session['id'])[0]
        count=[]
        countquestion = QASupport.objects.filter(userid=uid)
        for message in countquestion:
            data1.append(message.question_id)
        for qid in data1:
            unreadquestion = QASupport.objects.filter(question_id=qid).filter(read_question=0).filter(~Q(userid=uid))
            if(unreadquestion):
                count.append(len(unreadquestion))
                lastQues.append([unreadquestion.last().question_text, unreadquestion.last().userid.displayname, unreadquestion.last().question_date,unreadquestion.last().question_id])
        for qid in data1:
            unreadrepply = QAReplies.objects.filter(question_id=qid).filter(read_reply=0).filter(~Q(user_id=uid))
            if(unreadrepply):
                count.append(len(unreadrepply))
                lastmsgs.append([unreadrepply.last().reply_text, unreadrepply.last().userid.displayname, unreadrepply.last().reply_date,unreadrepply.last().reply_id])
        count = sum(count)
        print("Total msgs",count)
        context = {
            "Count": count,
            "Questions": lastQues,
            "Replies":lastmsgs

        }
        return context