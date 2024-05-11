# from django.contrib import admin
# from home.models import Contact
# from .models import Conference
# from .models import Workshop
# from .models import Concert
# from .models import Seminar
# from .models import CommunityMeetup
# # Register your models here.
# admin.site.register(Contact)

# admin.site.register(Conference)
# admin.site.register(Workshop)
# admin.site.register(Concert)
# admin.site.register(Seminar)
# admin.site.register(CommunityMeetup)


from django.contrib import admin
from home.models import Contact, Conference, Workshop, Concert, Seminar, CommunityMeetup, Event, Category


admin.site.register([Contact, Conference, Workshop, Concert, Seminar, CommunityMeetup, Event, Category])

    # Your custom admin configuration goes here


# 1-- models ko register kiya admin.py m
#     app k admn.py m jo bhi model banaya usko register karna h
# 2-- apps regster karna mtlb apps.py s copy karke naam ko paste it in 
#     settings.py -- installed_apps--- home.apps.HomeConfg  ---- apps to settings

