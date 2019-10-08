from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact, Talk, Course


#Utilizar o contat atraves do Speaker
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]  # Classes para o inline.
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        return format_html('<a href={0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_img.short_description = 'Foto'

    def email(self, obj):
        return obj.contact_set.emails().first()

        #return obj.contact_set(manager='emails').first()
        #return Contact.emails.filter(speaker=obj).first()
        #return Contact.objects.filter(kind=Contact.EMAIL, speaker=obj).first()

    email.short_description = 'e-mail'

    def phone(self, obj):
        return obj.contact_set.phones().first()
        #return obj.contact_set(manager='phones').first()
        #return Contact.phones.filter(speaker=obj).first()
        #return Contact.objects.filter(kind=Contact.PHONE, speaker=obj).first()

    phone.short_description = 'telefone'


class TalkModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(course=None)


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course)


