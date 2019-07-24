from django.contrib import admin

from org_api.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('founder', 'orgName')
    filter_horizontal = ('invitedUser',)


admin.site.register(Organization, OrganizationAdmin)
