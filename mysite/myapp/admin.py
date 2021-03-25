from django.contrib import admin
from .models import Companies, Designations, ProjectType, Languages, Databases, Frontend, Backend, VersionControls, \
    ReportTools, Projects, Trainings, Achievements

# Register your models here.


# class ProjectInline(admin.StackedInline):
#     model = Projects
#     extra = 1


class DesignationInline(admin.StackedInline):
    model = Designations
    extra = 1


class AddCompany(admin.ModelAdmin):
    inlines = [DesignationInline]


admin.site.register(Companies, AddCompany)
# admin.site.register(Designations)
admin.site.register(ProjectType)
admin.site.register(Languages)
admin.site.register(Databases)
admin.site.register(Frontend)
admin.site.register(Backend)
admin.site.register(VersionControls)
admin.site.register(ReportTools)
admin.site.register(Projects)
admin.site.register(Trainings)
admin.site.register(Achievements)
