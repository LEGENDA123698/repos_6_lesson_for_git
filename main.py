import django_settings

from myapp.models import User, Group


# user_1 = User(name='Sem', email = 'dam@gmail.com', role = "Admin")
# user_1.save()

# user_2 = User(name='Alex', email='alex@gmail.com', role='user')
# user_2.save()

# group = Group(group_name = "Samurai")




# group.groups.add(user_1, user_2)

# group.save()

user = User.objects.get(id=1)
group = Group.objects.get(id=1)

user.group.add(group)
