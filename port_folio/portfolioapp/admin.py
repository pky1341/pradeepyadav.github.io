from django.contrib import admin

from portfolioapp.models import (About, Contact, Etc, Image, Inf, Principle,
                                 Singing, Tutorial)

# Register your models here.
admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['name','img','upld_dt']
admin.site.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=['image','title','regular','wrk','techno','hstry']
admin.site.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display=['tutname','urlf']
admin.site.register(Inf)
class InfAdmin(admin.ModelAdmin):
    list_display=['info']
admin.site.register(Etc)
class EtcAdmin(admin.ModelAdmin):
    list_display=['passion_name','passion_url']
admin.site.register(Singing)
class SingAdmin(admin.ModelAdmin):
    list_display=['sname']
    
admin.site.register(Principle)
class PrincipleAdmin(admin.ModelAdmin):
    list_displa=["desc"]
    
admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','suggest']