from unltd.models import Group,GroupMember, User

class CreateGroup():
    request=''
    def __init__(self,req):
        self.request = req
    def Create_Group(self):
        user_id = self.request.session['id']
        title = self.request.POST.get("GroupName")
        description = self.request.POST.get("GroupDescription")
        GroupMembers_list = self.request.POST.getlist('GroupMembers[]')
        user = User.objects.filter(id=user_id)[0]
        print('AAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(user_id)
        print(title)
        print(description)
        print(GroupMembers_list)
        print('BBBBBBBBBBBBBBBBBBBBBBBBBBB')
        try:
            insert_group = Group(title=title, description=description, userid=user)
            insert_group.save()
            g_id = Group.objects.latest('group_id')
            new_group = Group.objects.filter(group_id=g_id)[0]
        except Exception as e:
            print(e)
            pass
        try:
            csv_file = self.request.FILES["csv_file"]
            file_data = csv_file.read().decode("utf-8")
            email_lists = []
            lines = file_data.split("\n")
            # loop over the lines and save them in db. If error , store as string and then display
            for line in lines:
                fields = line.split(",")
                email_lists.append(fields[0])
            print(email_lists)
            if email_lists ==0 and GroupMembers_list == 0:
                return -1
            for email in email_lists:
                print(email)
                if email is not None:
                    insert_members = GroupMember(email=email, group_id=g_id)
                    insert_members.save()
            return 1
        except Exception as e:
            print('EEEEEEEEEEEEEEEEEEEEEEEEE')
            print(e)
            print('EEEEEEEEEEEEEEEEEEEEEEEEE')
            pass
        try:
            for member in GroupMembers_list:
                member = int(member)
                member_reference = User.objects.filter(id=member)[0]
                insert_members = GroupMember(userid=member_reference, group_id=g_id)
                insert_members.save()
            return 1
        except Exception as e:
            print('SSSSSSSSSSSSSSSSS')
            print(e)
            print('SSSSSSSSSSSSSSSSS')
            return 0

    def get_all_members_with_group_by(self):
        data = []
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT user.Id, user.DisplayName,user.UserType FROM `user` where UserType != 'superadmin'")

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

