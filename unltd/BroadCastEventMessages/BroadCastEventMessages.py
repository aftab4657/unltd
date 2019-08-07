from unltd.models import Group,GroupMember, BroadCastEventMessages, User

class BroadCastEventMsg():
    request=''
    def __init__(self,req):
        self.request = req
    # THis is Broad Cast Messages Send
    def SendSMS(self):
        try:
            if (self.request.POST.get('send')):
                status = 'sent'
                st = 1
            else:
                status = 'draft'
                st = 2
            print(self.request.POST.get('send'))
            user_id = self.request.session['id']
            sms_text = self.request.POST.get('SmsText')
            sender = User.objects.filter(id=user_id)[0]
            type = 'BroadCast'
            print(user_id)
            Msgtype = 'SMS'
            brod_msdg = BroadCastEventMessages(description=sms_text,type=type,msgtype=Msgtype,senderid=sender,status=status)
            brod_msdg.save()
            return st
        except Exception as e:
            print(e)
            return 0


    def get_all_members_with_group_by(self):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT user.Id, user.DisplayName,user.UserType FROM `user` where UserType != 'superadmin' GROUP by UserType")

        for row in cursor.fetchall():
            data.append([row[0], row[1], row[2]])

        print(data)
        context = {
            "Data": data,
        }
        return context

    # THis method is to get all groups with all memeberss counters
    def get_all_groups(self):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT `group`.`GroupId`,`group`.`Title` , COUNT(group.GroupId) FROM `group` INNER JOIN groupmember on groupmember.GroupId = `group`.GroupId GROUP BY `group`.GroupId")

        for row in cursor.fetchall():
            data.append([row[0], row[1], row[2]])

        print(data)
        context = {
            "Data": data,
        }
        return context

