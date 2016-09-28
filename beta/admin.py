from django.contrib import admin
from beta.models import BetaTest, NewLetter
from beta.models import SignUp, Startup, Team, Tester, TestFeedBack, Info, Default

class BetaAdmin(admin.ModelAdmin):
    pass

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email', 'added_date')

class SignUpAdmin(admin.ModelAdmin):
    pass

class StartupAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'startup', 'stat',
                    'pub_status', 'added_date', 'pub_date')
    
    def get_name(self, obj):
        return "%s  %s" %(obj.user.first_name, obj.user.last_name)
    get_name.short_description = 'Name'

class TeamAdmin(admin.ModelAdmin):
    list_display = ('get_startup', 'full_name', 'role')
    
    def get_startup(self, obj):
        return obj.startup.startup
    get_startup.short_description = 'Startup'

class TesterAdmin(admin.ModelAdmin):
    pass

class TestFeedBackAdmin(admin.ModelAdmin):
    pass

#class ContactAdmin(admin.ModelAdmin):
#    pass

class InfoAdmin(admin.ModelAdmin):
    pass

class  DefaultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Default, DefaultAdmin)
admin.site.register(BetaTest, BetaAdmin)
admin.site.register(NewLetter, NewsLetterAdmin)
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Startup, StartupAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Tester, TesterAdmin)
admin.site.register(TestFeedBack, TestFeedBackAdmin)
#admin.site.register(Contact, ContactAdmin)
admin.site.register(Info, InfoAdmin)



